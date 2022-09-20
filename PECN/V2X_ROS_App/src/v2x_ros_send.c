#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <strings.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <errno.h>
#include <math.h>
#include "v2x_includes.h"
#include <cJSON.h>

#define MY_SEND_PORT 6800 // port 6800 is used to send messages
#define BUFF_LEN 1024
#define WMS_PORT 7202 // receive message from wms

char *SERVERIP = "127.0.0.1";
char *ROS_SERVER_IP_ADDR = "192.168.2.121"; // ROS server IP

char recvbuf[BUFF_LEN] = {0};
char sendbuf[BUFF_LEN] = {0};
static v2x_bsm_struct s_host_bsm;       
static v2x_bsm_struct s_remote_bsm;     

void send_to_ros(char* tx_buf, int tx_length)
{
    struct sockaddr_in servaddr;
    static int tx_count = 0;
    int cli_sock = -1;
    cli_sock = socket(PF_INET, SOCK_DGRAM, 0);
    // if((cli_sock = socket(PF_INET, SOCK_DGRAM, 0)) < 0)
    // {
    //     ERR_EXIT("socket");
    // }

    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family      = AF_INET;
    servaddr.sin_port        = htons(MY_SEND_PORT);
    servaddr.sin_addr.s_addr = inet_addr(ROS_SERVER_IP_ADDR);

    printf("send data to ros:[tx_count: %d length:%d] %s\n",tx_count, tx_length, tx_buf);
    sendto(cli_sock, tx_buf, tx_length, 0, (struct sockaddr *)&servaddr, sizeof(servaddr));
    tx_count += 1;
    close(cli_sock);

}


int main()
{
    int ret;
    int server_sock = -1;
    struct sockaddr_in server_addr;
    // IPV4 and UDP protocol
    server_sock = socket(AF_INET, SOCK_DGRAM, 0);    
    if(server_sock < 0){
        printf("create socket failed \n");
        return -1;
    }
    memset(&server_addr, 0 ,sizeof server_addr);
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    server_addr.sin_port = htons(WMS_PORT);
    // start listening MY_RECV_PORT
    ret = bind(server_sock, (struct sockaddr*)&server_addr, sizeof server_addr ); 
    if(ret < 0){
        printf("socket bind failed \n");
        return -1;
    }

    //monitor the socket status per 100ms
    fd_set readfds;
    struct timeval timeout = {0,0};
    int rx_count=0;
    int wait_count=0;
    while(1)
    {       
        // select timeout 100ms
        timeout.tv_sec = 0;
        timeout.tv_usec = 100000;

        // start monitoring sockets' status
        FD_ZERO(&readfds);
        FD_SET(server_sock, &readfds);
        int maxfd = server_sock + 1;
        ret = select(maxfd, &readfds, NULL, NULL, &timeout);

        if(FD_ISSET(server_sock, &readfds) > 0)
        {
            // server_sock is readable
            socklen_t len;
            int count = -1;
            struct sockaddr_in client_addr; 
            len = sizeof server_addr;
            char receive_buf[BUFF_LEN];
            memset(receive_buf, 0, BUFF_LEN); 
            // receive message
            count = recvfrom(server_sock, receive_buf, BUFF_LEN, 0, (struct sockaddr*)&server_addr, &len);// receive udp data
            if(count == -1)
            {
                printf("receive data failed!\n");
                return -1;	
            }
            rx_count++;
            printf("[rx_count: %d length:%d] %s\n", rx_count, count, receive_buf);
            //V2X_PR(LOG_LEVEL_DEBUG,LOG_ID,"[rx_count: %d length:%d] %s", rx_count, count, receive_buf);
            cJSON* root;
            //cJSON* format;
            root = cJSON_Parse(receive_buf);
            int value_int;
            double value_double;
            char* value_string;
            if (cJSON_GetObjectItem(root, "HostFlag") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "HostFlag")->valueint;
                if (value_int == 1)
                {
                    s_host_bsm.host_flag = VEH_FLAG_HOST;
                }
                else if (value_int == 2)
                {
                    s_host_bsm.host_flag = VEH_FLAG_REMOTE;
                }
                else
                {
                    s_host_bsm.host_flag = VEH_FLAG_NONE;
                }
            }
            //format = cJSON_GetObjectItem(root, "pos");
            if (cJSON_GetObjectItem(root, "Id") != NULL)
            {
                value_string = cJSON_GetObjectItem(root, "Id")->valuestring;
                strcpy(s_host_bsm.id, value_string);
                //s_host_bsm.id = value_string;
            }
            if (cJSON_GetObjectItem(root, "Latitude") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "Latitude")->valuedouble;
                s_host_bsm.pos.latitude = value_double;
            }
            if (cJSON_GetObjectItem(root, "Longitude") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "Longitude")->valuedouble;
                s_host_bsm.pos.longitude = value_double;
            }
            if (cJSON_GetObjectItem(root, "Elevation") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "Elevation")->valuedouble;
                s_host_bsm.pos.elevation = value_double;
            }
            if (cJSON_GetObjectItem(root, "SemiMajorAxisAccuracy") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "SemiMajorAxisAccuracy")->valuedouble;
                s_host_bsm.pos_acc.smajor_dev = value_double;
            }
            if (cJSON_GetObjectItem(root, "SemiMinorAxisAccuracy") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "SemiMinorAxisAccuracy")->valuedouble;
                s_host_bsm.pos_acc.sminor_dev = value_double;
            }
            if (cJSON_GetObjectItem(root, "SemiMajorAxisOrientation") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "SemiMajorAxisOrientation")->valuedouble;
                s_host_bsm.pos_acc.smajor_orien = value_double;
            }
            if (cJSON_GetObjectItem(root, "PostionConfidence") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "PostionConfidence")->valueint;
                s_host_bsm.pos_confidence.pos = value_int;        
            }            
            if (cJSON_GetObjectItem(root, "ElevationConfidence") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "ElevationConfidence")->valueint;
                s_host_bsm.pos_confidence.elevation = value_int;        
            }
            if (cJSON_GetObjectItem(root, "TransmissionState") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "TransmissionState")->valueint;
                s_host_bsm.trans = value_int;        
            }  
            if (cJSON_GetObjectItem(root, "Speed") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "Speed")->valuedouble;
                s_host_bsm.speed = value_double;
            }
            if (cJSON_GetObjectItem(root, "Heading") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "Heading")->valuedouble;
                s_host_bsm.heading = value_double;
            }
            if (cJSON_GetObjectItem(root, "SteeringWheelAngle") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "SteeringWheelAngle")->valueint;
                s_host_bsm.angle = value_int;        
            }
            //format = cJSON_GetObjectItem(root, "accel_set"); 
            if (cJSON_GetObjectItem(root, "LongitudalAcceleration") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "LongitudalAcceleration")->valuedouble;
                s_host_bsm.accel_set.acc_lng = value_double;
            }
            if (cJSON_GetObjectItem(root, "LateralAcceleration") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "LateralAcceleration")->valuedouble;
                s_host_bsm.accel_set.acc_lat = value_double;
            }
            if (cJSON_GetObjectItem(root, "VerticalAcceleration") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "VerticalAcceleration")->valuedouble;
                s_host_bsm.accel_set.acc_vert = value_double;
            }
            if (cJSON_GetObjectItem(root, "YawRate") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "YawRate")->valuedouble;
                s_host_bsm.accel_set.yaw_rate = value_double;
            }
            if (cJSON_GetObjectItem(root, "BrakePadel") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "BrakePadel")->valueint;
                s_host_bsm.brakes.brake_padel = value_int;        
            } 
            if (cJSON_GetObjectItem(root, "WheelBrakes") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "WheelBrakes")->valueint;
                s_host_bsm.brakes.wheel_brakes = value_int;        
            } 
            if (cJSON_GetObjectItem(root, "Traction") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "Traction")->valueint;
                s_host_bsm.brakes.traction = value_int;        
            } 
            if (cJSON_GetObjectItem(root, "ABS") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "ABS")->valueint;
                s_host_bsm.brakes.abs = value_int;        
            }
            if (cJSON_GetObjectItem(root, "SCS") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "SCS")->valueint;
                s_host_bsm.brakes.scs = value_int;        
            } 
            if (cJSON_GetObjectItem(root, "BrakeBoost") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "BrakeBoost")->valueint;
                s_host_bsm.brakes.brake_boost = value_int;        
            }
            if (cJSON_GetObjectItem(root, "AuxBrakes") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "AuxBrakes")->valueint;
                s_host_bsm.brakes.aux_brakes = value_int;        
            }   
            if (cJSON_GetObjectItem(root, "Width") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "Width")->valuedouble;
                s_host_bsm.veh_size.width = value_double;
            }
            if (cJSON_GetObjectItem(root, "Length") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "Length")->valuedouble;
                s_host_bsm.veh_size.length = value_double;
            }
            if (cJSON_GetObjectItem(root, "Height") != NULL)
            {
                value_double = cJSON_GetObjectItem(root, "Height")->valuedouble;
                s_host_bsm.veh_size.height = value_double;
            }
            if (cJSON_GetObjectItem(root, "BasicVehicleClass") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "BasicVehicleClass")->valueint;
                s_host_bsm.vehicle_classification.classification = value_int;        
            }   
            if (cJSON_GetObjectItem(root, "FuelType") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "FuelType")->valueint;
                s_host_bsm.vehicle_classification.fuel_type = value_int;        
            }  
            if (cJSON_GetObjectItem(root, "Events") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "Events")->valueint;
                s_host_bsm.events = value_int;        
            }
            if (cJSON_GetObjectItem(root, "Light") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "Light")->valueint;
                s_host_bsm.lights = value_int;        
            }
            //format = cJSON_GetObjectItem(root, "veh_emergency_ext");               
            if (cJSON_GetObjectItem(root, "ResponseType") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "ResponseType")->valueint;
                s_host_bsm.veh_emergency_ext.response_type = value_int;        
            } 
            if (cJSON_GetObjectItem(root, "SirenInUse") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "SirenInUse")->valueint;
                s_host_bsm.veh_emergency_ext.siren_use = value_int;        
            }  
            if (cJSON_GetObjectItem(root, "LightbarInUse") != NULL)
            {
                value_int = cJSON_GetObjectItem(root, "LightbarInUse")->valueint;
                s_host_bsm.veh_emergency_ext.lights_use = value_int;        
            }                           

            // send message to wms
            send_to_ros(receive_buf,count);
            //V2X_PR(LOG_LEVEL_DEBUG,LOG_ID,"Sending to WMS");
        }
        else if(FD_ISSET(server_sock, &readfds)==0)
        {
            // server sock is unreadable
            wait_count++;
            if(wait_count == 10){
                printf("waiting\n");
                wait_count = 0;
            }
            
        }
        else
        {
            // error
            printf(" socket error\n");
            return -1;
        }
    }
}