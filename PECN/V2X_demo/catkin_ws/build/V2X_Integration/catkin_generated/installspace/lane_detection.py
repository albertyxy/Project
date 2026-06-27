#!/usr/bin/env python2

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import Int16MultiArray
from cv_bridge import CvBridge
from PIL import Image as PIL


def cam_callback(image):
    global lane_line_pub
    global lane_line_image_pub

    # read image from buffer, convert to 1-dimensional array
    array = np.frombuffer(image.data, dtype=np.dtype("uint8"))

    # reshape the 1-dimensional array to 4-dimensional array, 480 x 640 RGBalpha
    array = np.reshape(array, (image.height, image.width, 4))

    # discard alpha information, RGB only
    array = array[:, :, :3]

    # array = array[:, :, ::-1] # RGB to BGR

    # define the array that store the left and right line
    left = []
    right = []

    # copy array to img_copy to avoid RAM error
    img_copy = np.copy(array)
    roi = img_copy[0:700, 0:1024]

    # gray_img = cv2.cvtColor(img_copy, cv2.COLOR_RGB2GRAY)
    # hsl_img = cv2.cvtColor(img_copy, cv2.COLOR_RGB2HLS)

    # # generate yellow mask in HLS format
    # yellow_lower = np.uint8([10, 0, 100])
    # yellow_upper = np.uint8([40, 255, 255])
    # yellow_mask = cv2.inRange(hsl_img, yellow_lower, yellow_upper)

    # # generate white mask in HLS format
    # white_lower = np.array([0, 200, 0])
    # white_upper = np.array([255, 255, 255])
    # white_mask = cv2.inRange(hsl_img, white_lower, white_upper)

    # # OR the mask info
    # mask = cv2.bitwise_or(yellow_mask, white_mask)

    # # process the img_copy with mask above
    # processed_img = cv2.bitwise_and(img_copy, img_copy, mask=mask)

    # process the masked img with gaussian blur to decrease noise
    # lenna = cv2.GaussianBlur(roi, (3, 3), 0)
    lenna = cv2.GaussianBlur(roi, (7, 7), 0)

    # get the edges info using canny method
    # edges = cv2.Canny(lenna, 150, 200)
    edges = cv2.Canny(lenna, 120, 200)

    # find lines using hough transform
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 120)
    # lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)
    # lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, 1000, 10)

    # if there are lines in the processed img then draw the line
    # Hough Line Transform, not probablistic version
    if lines is not None:
        if lines.size > 0:
            for line in lines:
                rho,theta = line[0]
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                if b > 0.2 and b < 0.8:
                    if a < 0:
                        # if a < 0, (x0, y0) would be presented over the displayed -> y0 would be negative
                        x1 = int(x0 - 500 * (-b))
                        y1 = int(y0 - 500 * (a))
                        x2 = int(x0 - 1100 * (-b))
                        y2 = int(y0 - 1100 * (a))
                        if x1 < 600 and x1 > 400 and (y2 - y1) > 400:
                            right.append((x1, y1, x2, y2))
                            # cv2.line(img_copy, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    else:
                        x1 = int(x0 + 450*(-b))
                        y1 = int(y0 + 450*(a))
                        x2 = int(x0 - 150*(-b))
                        y2 = int(y0 - 150*(a))
                        if x2 < 600 and x2 > 400 and (y1 - y2) > 400:
                            left.append((x1, y1, x2, y2))
                            # cv2.line(img_copy,(x1, y1), (x2, y2),(0,0,255),2)

    # take average
    left_average = [0, 0, 0, 0]
    for coordinate in left:
        left_average = [left_average[i] + coordinate[i] for i in range(4)]
    if len(left) != 0:
        for i in range(4):
            left_average[i] = left_average[i] // len(left)
        cv2.line(img_copy, (left_average[0] + 10, left_average[1]), (left_average[2] + 10, left_average[3]), (0, 0, 255), 2)
        cv2.line(img_copy, (left_average[0] - 10, left_average[1]), (left_average[2] - 10, left_average[3]), (0, 0, 255), 2)

    right_average = [0, 0, 0, 0]
    for coordinate in right:
        right_average = [right_average[i] + coordinate[i] for i in range(4)]
    if len(right) != 0:
        for i in range(4):
            right_average[i] = right_average[i] // len(right)    
        cv2.line(img_copy, (right_average[0] + 10, right_average[1]), (right_average[2] + 10, right_average[3]), (0, 0, 255), 2)
        cv2.line(img_copy, (right_average[0] - 10, right_average[1]), (right_average[2] - 10, right_average[3]), (0, 0, 255), 2)
    
    msg = left_average + right_average
    msg_pub = Int16MultiArray(data=msg)
    lane_line_pub.publish(msg_pub)
    bridge = CvBridge()
    img_pub = bridge.cv2_to_imgmsg(img_copy, encoding="passthrough")
    lane_line_image_pub.publish(img_pub)


    # image.data = img_flatten
    # lane_line_image_pub.publish(image)

    # Hough Line Transform, probablistic version
    # if lines is not None:
    #     if lines.size > 0:
    #         for line in lines:
    #             x1, y1, x2, y2 = line[0]
    #             cv2.line(img_copy, (x1, y1), (x2, y2), (0, 0, 255), 4)

    # display the processed img using cv2 imshow
    # FL
    # if cam_index == 0:
    #     img_copy = np.rot90(img_copy)
    # elif cam_index == 1:
    #     img_copy = np.rot90(img_copy)
    #     img_copy = np.rot90(img_copy)
    #     img_copy = np.rot90(img_copy)
    # elif cam_index  == 3:
    #     img_copy = np.rot90(img_copy)
    #     img_copy = np.rot90(img_copy)


    # cv2.imshow("Front Camera", img_copy)
    # # cv2.imshow(cam_number[cam_index] + "raw", processed_img)
    # # cv2.imshow(cam_number[cam_index] + " edges", edges)
    # cv2.waitKey(1)

def display():
    global lane_line_pub
    global lane_line_image_pub
    lane_line_pub = rospy.Publisher('lane_line', Int16MultiArray, queue_size=100)
    lane_line_image_pub = rospy.Publisher('lane_line_image', Image, queue_size=100)
    rospy.init_node('display', anonymous=True)
    rospy.Subscriber("/carla/hero/FrontCam/image", Image, cam_callback)
    # rospy.Subscriber("carla/hero/camera/rgb/FrontCam/image_color", Image, cam_callback)
    rospy.spin()

if __name__ == '__main__':
    display()