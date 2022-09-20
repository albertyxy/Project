# Author Nissi Varghese, Intern at Porsche Engineering Service
# create the signal generator function 
# Include the all the BSM data
# Send BSM data To PEVATeC simulator through ROS driver to Saftey Function
# In saftey function will receive simualted signals from PEVATeC.
# then action should be triggered
# To display on dashboard

#/usr/bin/python3

#input all the modules

import json
import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import socket




#Here the class holds all the BSM messages

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dest_addr = ('10.0.2.15', 7000) 
class V2X_BSM(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title("SIGNAL GENERATOR")
        self.geometry("4000x4000")
        #self.resizable(False,False)
        self.msgCnt = IntVar()
        self.id = StringVar()
        self.secMark = IntVar()
        self.heading =StringVar()
        self.heading_range = DoubleVar()
        self.speed_range = DoubleVar()
        self.speed = StringVar()
        self.angle = StringVar()
        self.angle_range = IntVar()
        self.size =DoubleVar()
        self.host_flag = IntVar()
        #self.path_his =PathHistory()
        #self.path_pre =PathPrediction
        # essential to enable full window resizing
        self.running=True
     

    #GUI for canvas and scrollbar
        #Create a Frame 
        self.Main_frame =Frame(self)
        self.Main_frame.grid(sticky='news')
        self.canvas = Canvas(self)
        self.canvas.grid(row=10,column=9,sticky=N+S)
        self.canvas.grid_propagate(False)
        self.canvas.grid_rowconfigure(0, weight=1)
        self.canvas.grid_columnconfigure(0, weight=1)
         # 3) Scroll Sidebar also goes inside this frame in next column
        self.second_frame = Frame(self)
        self.scroll_y = Scrollbar(self, orient='vertical')
        self.scroll_y.grid(row=40, column=1, sticky=N+S)
        self.scroll_x = Scrollbar(self,orient='horizontal')
        self.scroll_x.grid(row=40, column=2, sticky=E+W)
        self.canvas.configure(yscrollcommand =self.scroll_y.set)
        self.canvas.configure(xscrollcommand=self.scroll_x.set)
        self.scroll_y.config(command =self.canvas.yview)
        self.scroll_x.config(command =self.canvas.xview)
        self.canvas.create_window((5,5) ,window=self.second_frame, anchor='nw',tags="my_tag")
        self.canvas.bind('<Configure>', lambda : self.canvas.configure(scrollregion =self.canvas.bbox("all")))
        #host flag
        self.host_flag_choice=["None","Host Vehicle","Remote Vehicle"]
        self.label0 =Label(self.second_frame,text="Host Flag",font=('Helvetica', 10, 'bold')).grid(row=0,column=0,padx=5,pady=5)
        self.entry0 = Entry(self.second_frame,textvariable=self.host_flag).grid(row=0,column=2,padx=5,pady=5)
        self.comboflag =ttk.Combobox(self.second_frame,values=self.host_flag_choice)
        self.comboflag.bind("<<ComboboxSelected>>",self.selectedhost)
        self.comboflag.grid(row=0,column=1)
        self.comboflag.set("None")

        #message count
        self.label1 = Label(self.second_frame,text="Message Count",font=('Helvetica', 10, 'bold')).grid(row=1,column=0,padx=5,pady=5)
        Label(self.second_frame,text='Define Message Count: The sender numbers similar messages it sends in sequence from 0,127 circularly. \n',fg ='red',font= ('Aerial', 8)).grid(row=1,column=5,sticky =W)
        self.entry1 = Entry(self.second_frame,textvariable=self.msgCnt).grid(row=1,column=1,padx=5,pady=5)
        self.scale=Scale(self.second_frame,variable=self.msgCnt,from_=0, to=127, orient=HORIZONTAL).grid(row=1, column=2)
        #Label(self.second_frame,text='south').grid(row=1, column=2)
        self.canvas.grid_rowconfigure(1,weight=1)
        self.canvas.grid_columnconfigure(1,weight=1)


        #ID
        self.label2 = Label(self.second_frame,text="ID",font=('Helvetica', 10, 'bold')).grid(row=2,column=0,padx=5,pady=5)
        self.entry2 = Entry(self.second_frame,textvariable=self.id).grid(row=2,column=1,padx=5,pady=5)
        Label(self.second_frame,text='Define ID: Id of the vehicle.\n',fg ='red',font= ('Aerial', 8)).grid(row=2,column=5,sticky =W)

        #Timestamp
        self.label3 = Label(self.second_frame,text="Time Stamp",font=('Helvetica', 10, 'bold')).grid(row=3,column=0,padx=5,pady=5)
        self.entry3 = Entry(self.second_frame,textvariable=self.secMark).grid(row=3,column=1,padx=5,pady=5)

        #Position
        self.label4 = Label(self.second_frame,text="Position",font=('Helvetica', 10, 'bold')).grid(row=4,column=0,padx=5,pady=5)

        #Postion Accuracy
        self.label8 = Label(self.second_frame,text="Positional Accuracy",font=('Helvetica', 10, 'bold')).grid(row=8,column=0,padx=5,pady=5)

        #Transmission state
        self.label12 = Label(self.second_frame,text="Transmission State",font=('Helvetica', 10, 'bold')).grid(row=12,column=0,padx=5,pady=5)

        #Heading
        self.label13 = Label(self.second_frame,text='Heading',font=('Helvetica', 10, 'bold')).grid(row=13,column=0,padx=5,pady=5)
        self.entry13= Entry(self.second_frame,textvariable=self.heading).grid(row=13,column=1)
        self.scale=Scale(self.second_frame,variable=self.heading_range,from_=0,to=28800, orient=HORIZONTAL,command=lambda e :self.heading.set(float(e)*0.0125)).grid(row=13, column=3)
        Label(self.second_frame,text ='Degree').grid(row=13,column=2)
        Label(self.second_frame,text='Define the Heading.The heading angle of the vehicle or traffic participant.\n It is the clockwise angle between the direction of motion and the true north direction.The resolution is 0.0125°. The Value Range is 0,28800',fg ='red',font= ('Aerial', 8)).grid(row=13,column=5,sticky =W)

        #Speed
        self.label14 = Label(self.second_frame,text='Speed',font=('Helvetica', 10, 'bold')).grid(row=14,column=0,padx=5,pady=5)
        self.scale=Scale(self.second_frame,variable=self.speed_range,from_=0, to=8191, orient=HORIZONTAL,command=lambda e :self.speed.set(float(e)*0.02)).grid(row=14, column=3) #scale slider
        Label(self.second_frame,text='The speed of vehicles.The resolution is 0.02m/s.The value range is 0,8191 and 8191 represents an invalid value',fg ='red',font= ('Aerial', 8)).grid(row=14,column=5,sticky =W)
        Label(self.second_frame,text ='m/s').grid(row=14,column=2)
        self.entry14 = Entry(self.second_frame,textvariable=self.speed).grid(row=14,column=1)

        #Angle
        self.label15 = Label(self.second_frame,text='Angle',font=('Helvetica', 10, 'bold')).grid(row=15,column=0,padx=5,pady=5)
        self.entry15 = Entry(self.second_frame,textvariable=self.angle).grid(row=15,column=1)
        Label(self.second_frame,text='Define the vehicle steering wheel angle. It is positive to the right, and negative to the left.The resolution is 1.5°.The value Range is -126,127 ',fg ='red',font= ('Aerial', 8)).grid(row=15,column=5,sticky =W)
        self.scale=Scale(self.second_frame,variable=self.angle_range,from_=-126, to=126, orient=HORIZONTAL,command=lambda e :self.angle.set(float(e)*1.5)).grid(row=15, column=3)
        Label(self.second_frame,text ='Degree').grid(row=15,column=2)
        
        # Acceleration set
        self.label16 = Label(self.second_frame,text='Acceleration Set',font=('Helvetica', 10, 'bold')).grid(row=16,column=0,padx=5,pady=5)

        #Brake System Status
        self.label10 = Label(self.second_frame,text='Brake System Status',font=('Helvetica', 10, 'bold')).grid(row=21,column=0,padx=5,pady=5)

        #Vechicle Size
        self.label21 = Label(self.second_frame,text='Vehcile Size',font=('Helvetica', 10, 'bold')).grid(row=23,column=0,padx=5,pady=5)
        Label(self.second_frame,text='size of the vehicle. It is defined by three dimensions of vehicle length, width and height, where the height value is optional.',fg ='red',font= ('Aerial', 8)).grid(row=23,column=5,sticky =W)
        
        #Vehicle Classification
        self.label25 = Label(self.second_frame,text='Vehcile Classification',font=('Helvetica', 10, 'bold')).grid(row=27,column=0,padx=5,pady=5)
        Label(self.second_frame,text ='Define the vehicle classification. Vehicle types can be defined from various dimensions and including the basic vehicle types and fuel power types.',fg ='red',font= ('Aerial', 8)).grid(row=27,column=5,sticky =W)

        #Vehcile Emergency Extension
        self.label28 = Label(self.second_frame,text='Vehcile Emergency Extension',font=('Helvetica', 10, 'bold')).grid(row=30,column=0,padx=5,pady=5)
        Label(self.second_frame,text='Auxiliary information set for emergency vehicles or special vehicles. \n It is used in BSM messages to inform the surrounding vehicles of the status of special operations of any emergency vehicle or special vehicle,\n remind them to give priority or keep clear',fg ='red',font= ('Aerial', 8)).grid(row=30,column=5,sticky =W)
        
        
        self.label31 = Label(self.second_frame,text='Events',font=('Helvetica', 10, 'bold')).grid(row=34,column=0,padx=5,pady=5)
        self.label32 = Label(self.second_frame,text='Lights',font=('Helvetica', 10, 'bold')).grid(row=35,column=0,padx=5,pady=5)
        self.labeö33 = Label(self.second_frame,text='Position Confidence',font=('Helvetica', 10, 'bold')).grid(row=36,column=0,padx=5,pady=5)
    def selectedhost(self,events):

        if self.comboflag.get() =="None":
          self.host_flag.set(0)
        elif self.comboflag.get() =="Host Vehicle":
            self.host_flag.set(1)
        elif self.comboflag.get() =="Remote Vehicle":
            self.host_flag.set(2)
  
   
class Position(V2X_BSM): 

    def __init__(self):
        #V2X_BSM.__init__(self)
        super().__init__()
        self.Lat=StringVar()
        self.Lat_range = DoubleVar()
        #self.Lat.set('00.000')
        self.long =StringVar()
        self.Long_range = DoubleVar()
        self.ele = StringVar()
        self.ele_range = DoubleVar()
        #self.labels =Label(self.second_frame)
   
        self.label5 = Label(self.second_frame,text="Latitude:").grid(row=5,column=0,padx=5,pady=5)
        self.entry5 = Entry(self.second_frame,textvariable=self.Lat).grid(row=5,column=1)
        Label(self.second_frame,text='Vehicle position,Latitudes specify the north-south position of a location.The Value Range is -900000000,900000001',fg ='red',font= ('Aerial', 8)).grid(row=5,column=5,sticky =W)
        Label(self.second_frame,text ='Decimal Degree ').grid(row=5,column=2)
        self.label6 = Label(self.second_frame,text="Longitude:").grid(row=6,column=0,padx=5,pady=5)
        self.entry6 = Entry(self.second_frame,textvariable=self.long).grid(row=6,column=1)
        Label(self.second_frame,text='Define the longitude value.East longitude is positive and west longitude is negative.The resolution is -7°.The Value Range is -1799999999,1800000001',fg ='red',font= ('Aerial', 8)).grid(row=6,column=5,sticky =W) 
        Label(self.second_frame,text ='Decimal Degree').grid(row=6,column=2)
        self.label7 = Label(self.second_frame,text="Elevation:").grid(row=7,column=0,padx=5,pady=5)
        Label(self.second_frame,text='Define the vehicle elevation.The resolution is 0.1m.The Value Range is -4096,61439',fg ='red',font= ('Aerial', 8)).grid(row=7,column=5,sticky =W) 
        Label(self.second_frame,text ='Meters ').grid(row=7,column=2)
        #Label(self.second_frame,text ='North').grid(row=5,column=3)
        self.entry7 = Entry(self.second_frame,textvariable=self.ele).grid(row=7,column=1)
        self.scale=Scale(self.second_frame,variable=self.Lat_range ,from_=-900000000, to=900000001, orient=HORIZONTAL,command=lambda e :self.Lat.set(float(e)/10000000)).grid(row=5, column=3)
        #Label(self.second_frame,text ='North').grid(row=5,column=3)

        #Label(self.second_frame,text ='South').grid(row=5,column=5)
    


        self.scale=Scale(self.second_frame,variable=self.Long_range,from_= -1799999999, to=1800000001, orient=HORIZONTAL,command=lambda e :self.long.set(float(e)/10000000)).grid(row=6, column=3)
        self.scale=Scale(self.second_frame,variable=self.ele_range,from_= -4096, to=61439, orient=HORIZONTAL,command=lambda e :self.ele.set(float(e)/10)).grid(row=7, column=3)
 
class PositionalAccuracy(Position):

    def __init__(self):
        super().__init__()
        self.semimajor = StringVar() 
        self.semimajor_range =DoubleVar()
        self.semiminor =  StringVar()  
        self.semiminor_range =DoubleVar()
        self.orient = StringVar() 
        self.orient_range = DoubleVar()

        self.label9 = Label(self.second_frame,text='Semi Major Axis Accuracy').grid(row=9,column=0,padx=5,pady=5)
        self.entry9 = Entry(self.second_frame,textvariable= self.semimajor ).grid(row=9,column=1)
        Label(self.second_frame,text ='Meters').grid(row=9,column=2)
        self.scale=Scale(self.second_frame,variable=self.semimajor_range,from_=0, to= 255, orient=HORIZONTAL,command=lambda e :self.semimajor.set(float(e)/20)).grid(row=9, column=3)

        #Semi minor
        self.label10 = Label(self.second_frame,text='Semi Minor Axis Accuracy').grid(row=10,column=0,padx=5,pady=5)
        self.entry10 = Entry(self.second_frame,textvariable= self.semiminor).grid(row=10,column=1)
        Label(self.second_frame,text ='Meters').grid(row=10,column=2)
        self.scale=Scale(self.second_frame,variable=self.semiminor_range,from_=0, to= 255, orient=HORIZONTAL,command=lambda e :self.semiminor.set(float(e)/20)).grid(row=10, column=3)
        
        #semi orientation 
        self.label11 = Label(self.second_frame,text='Semi Major Axis Orientation').grid(row=11,column=0,padx=5,pady=5)
        Label(self.second_frame,text ='Degree').grid(row=11,column=2)
        self.entry10 = Entry(self.second_frame,textvariable= self.orient).grid(row=11,column=1)
        self.scale=Scale(self.second_frame,variable= self.orient_range,from_=0, to=65535, orient=HORIZONTAL,command=lambda e :self.orient.set(float(e)*0.0054932479)).grid(row=11, column=3)
        Label(self.second_frame,text='Positional Accuracy is : The accuracy of positioning system based on an elliptic model',fg ='red',font= ('Aerial', 8)).grid(row=8,column=5,sticky =W)
        Label(self.second_frame,text='Define the size of the semi-major axis in GNSS system accuracy expressed by an elliptic model. The numerical resolution is 0.05m.TheValue Range is 0,255',fg ='red',font= ('Aerial', 8)).grid(row=9,column=5,sticky =W)
        Label(self.second_frame,text='Defines the size of semi-minor axis in GNSS system accuracy expressed by elliptic model.The numerical resolution is 0.05m.The Value Range is 0,255',fg ='red',font= ('Aerial', 8)).grid(row=10,column=5,sticky =W)
        Label(self.second_frame,text='Define the included angle from the true north clockwise to the nearest semi-major axis in the GNSS system accuracy expressed by elliptic model.\n The Value Range is 0,65535',fg ='red',font= ('Aerial', 8)).grid(row=11,column=5,sticky =W)

class AccelerationSet4way(PositionalAccuracy):

    def __init__(self):
        super().__init__()
        self.Acc_Lat = StringVar() 
        self.Acc_Lat_range =DoubleVar()
        self.Acc_Lng = StringVar() 
        self.Acc_Lng_range =DoubleVar()
        self.Acc_Vert = StringVar() 
        self.Acc_Vert_range =DoubleVar()
        self.Yaw_rate =StringVar() 
        self.Yaw_rate_range =DoubleVar()

        # Lateral Acceleration
        self.label17 = Label(self.second_frame,text="Lateral Acceleration").grid(row=17,column=0,padx=5,pady=5)
        self.entry17 = Entry(self.second_frame,textvariable=self.Acc_Lat).grid(row=17,column=1)
        Label(self.second_frame,text ='m/s^2').grid(row=17,column=2)
        self.scale  = Scale(self.second_frame,variable=self.Acc_Lat_range,from_= -2000, to=2001, orient=HORIZONTAL,command=lambda e :self.Acc_Lat.set(float(e)*0.01)).grid(row=17, column=3)
        Label(self.second_frame,text=' Lateral Acceleration: The acceleration along the Y axis or perpendicular to the vehicle s general direction of travel in parallel with a left-to-right centerline.\n The Units of 0.01 m/s^2 where negative values indicate the vehicle is accelerating to left.The value Range is -2000,2001 \n',fg ='red',font= ('Aerial', 8)).grid(row=17,column=5,sticky =W)
        
        #Longitudual Acceleration
        self.label18= Label(self.second_frame,text="Longitudal Acceleration").grid(row=18,column=0,padx=5,pady=5)
        self.entry18 = Entry(self.second_frame,textvariable=self.Acc_Lng ).grid(row=18,column=1)
        self.scale  = Scale(self.second_frame,variable=self.Acc_Lng_range,from_= -2000, to=2001, orient=HORIZONTAL,command=lambda e :self.Acc_Lng.set(float(e)*0.01)).grid(row=18, column=3)
        Label(self.second_frame,text ='m/s^2').grid(row=18,column=2)
        Label(self.second_frame,text='Longitudinal acceleration: Forward acceleration is positive, and reverse acceleration is negative.The resolution is 0.01 m/s^2.The value Range is -2000,2001\n',fg ='red',font= ('Aerial', 8)).grid(row=18,column=5,sticky =W)
        
        #Vertical  Acceleration
        self.label19= Label(self.second_frame,text="Vertical Acceleration").grid(row=19,column=0,padx=5,pady=5)
        self.entry19 = Entry(self.second_frame,textvariable=self.Acc_Vert ).grid(row=19,column=1)
        Label(self.second_frame,text ='Gravity').grid(row=19,column=2)
        Label(self.second_frame,text='Define the acceleration in the Z-axis direction, which is vertically downward and positive along the Z-axis direction.\n The resolution is 0.02G, and G is the gravity acceleration value of 9.80665m/s2. The value Range is -127,127 \n',fg ='red',font= ('Aerial', 8)).grid(row=19,column=5,sticky =W)
        self.scale  = Scale(self.second_frame,variable=self.Acc_Vert_range,from_= -127, to= 127, orient=HORIZONTAL,command=lambda e :self.Acc_Vert.set(float(e)*0.02)).grid(row=19, column=3)
        
        #Yaw Rate
        self.label20= Label(self.second_frame,text="Yaw Rate").grid(row=20,column=0,padx=5,pady=5)
        self.entry20 = Entry(self.second_frame,textvariable=self.Yaw_rate ).grid(row=20,column=1)
        Label(self.second_frame,text ='Degrees Per Second').grid(row=20,column=2)
        Label(self.second_frame,text=' Define the yaw rate. It refers to the deflection of the vehicle from the vertical axis. \n It is positive for clockwise rotation and negative for anti-clockwise rotation. The data resolution is 0.01°/s. The  Value Range is -32767,32767',fg ='red',font= ('Aerial', 8)).grid(row=20,column=5,sticky =W)
        self.scale=Scale(self.second_frame,variable=self.Yaw_rate_range ,from_=-32767, to=32767, orient=HORIZONTAL,command=lambda e :self.Yaw_rate.set(float(e)*0.01)).grid(row=20, column=3)   
'''
Define the brake system status of the vehicle. The following 7 different status types are
included:
 brakePadel: brake pedal depressed;
 wheelBrakes: wheel brake applied;
 Traction: functioning of traction control system.
 abs: functioning of anti-lock braking system.
 scs: functioning of body stability control system.
 brakeBoost: brake boost applied.
 auxBrakes: auxiliary brake status (generally referred to as handbrake).

'''

class BrakeSystemStatus(AccelerationSet4way):

    def __init__(self):
        super().__init__()
        self.brakes = IntVar()
        self.abs=IntVar()
        self.aux_brakes =IntVar()
        self.brake_boost =IntVar()
        self.brake_padel =IntVar()
        self.scs =IntVar()
        self.traction =IntVar()
        self.wheel_brakes =IntVar()
        self.brake_choice=["brakePadel","wheelBrakes","traction","abs","scs","brakeBoost","auxBrakes"]
        self.combobrake =ttk.Combobox(self.second_frame,values=  self.brake_choice)
        self.combobrake.bind("<<ComboboxSelected>>",self.selectedbrakes)
        self.combobrake.grid(row=21, column=1)
        self.combobrake.set("Brake Padel")
        self.status = Entry(self.second_frame,textvariable=self.abs).grid(row=21,column=2)
       
        Label(self.second_frame,text=' Define Brake System status.The brake pedal is depressed.\n vehicle wheel braking.\n Anti-lock braking system working.\n Functioning of traction control system.\n Functioning of body stability control system,\n brake boost applied.\n Auxiliary brake status (Hand Brake)',fg ='red',font= ('Aerial', 8)).grid(row=21,column=5,sticky =W)
        Label(self.second_frame,text=' * Unavailable - 0.\n OFF - 1.\n ON - 2 .\n Engaged -3',fg ='red',font= ('Aerial', 8)).grid(row=21,column=3,sticky =W)

    def selectedbrakes(self,events):
        if self.combobrake.get() =="brakePadel":
           self.abs.set(0)
        elif self.combobrake.get() =="wheelBrakes":
            self.abs.set(1)
        elif self.combobrake.get() =="traction":
            self.abs.set(2)
        elif self.combobrake.get() =="abs":
            self.abs.set(3)
        elif self.combobrake.get() =="scs":
            self.abs.set(0)
        elif self.combobrake.get() =="brakeBoost":
            self.abs.set(1)
        elif self.combobrake.get() =="auxBrakes":
            self.abs.set(3)



#transmissionState ::= ENUMERATED {
#    neutral         (0), -- Neutral
#    park            (1), -- Park
#    forwardGears    (2), -- Forward gears
#    reverseGears    (3), -- Reverse gears
#    reserved1       (4),      
#    reserved2       (5),      
#    reserved3       (6),      
#    unavailable     (7), -- not-equipped or unavailable value,
#    }



class TransmissionState(BrakeSystemStatus):

    def __init__(self):
        super().__init__()

    
        self.trans =StringVar(self.second_frame)
        self.entryoptout=IntVar(self.second_frame)
        self.neutral= IntVar()
        self.park =  IntVar()
        #self.output = DoubleVar()
        self.forwardGears =  IntVar()
        self.reverseGears =  IntVar()   

        self.choice_one= ["neutral","park","forwardGears","reverseGears","reserved1","reserved2","reserved3","unavailable"]
        self.choice_two = [0,1,2,3,4,5,6,7]
        self.combo1 =ttk.Combobox(self.second_frame,values= self.choice_one)

        self.combo1.bind("<<ComboboxSelected>>",self.selectedtrans)
        self.combo1.grid(row=12, column=1)
        self.entryopt = Entry(self.second_frame,textvariable=self.entryoptout).grid(row=12,column=2)
        self.combo1.set("neutral")
        Label(self.second_frame,text=' * Neutral - 0.\n park - 1.\n Forward Gears - 2.\n Reverse Gears - 3.\n Reserved1 - 4.\n Reserved2 - 5.\n Reserved 3 - 6.\n Unavailable- 7',fg ='red',font= ('Aerial', 8)).grid(row=12,column=3)
    def selectedtrans(self,events):
        if self.combo1.get() =="neutral":
           self.entryoptout.set(0)
        elif self.combo1.get() =="park":
            self.entryoptout.set(1)
        elif self.combo1.get() =="forwardGears":
            self.entryoptout.set(2)
        elif self.combo1.get() =="reverseGears":
            self.entryoptout.set(3)
        elif self.combo1.get() =="reserved1":
            self.entryoptout.set(4)
        elif self.combo1.get() =="reserved2":
            self.entryoptout.set(5)
        elif self.combo1.get() =="reserved3":
            self.entryoptout.set(6)
        elif self.combo1.get() =='unavailable':
            self.entryoptout.set(7)
  

class VehicleSize(TransmissionState):

    def __init__(self):
        super().__init__()
        self.height = StringVar()
        self.height_range = DoubleVar()
        self.width = DoubleVar()
        self.width_range = StringVar()
        self.length =DoubleVar()
        self.length_range =StringVar()

        #Height
        self.label22 = Label(self.second_frame,text='Height').grid(row=24,column=0,padx=5,pady=5)
        self.entry22 = Entry(self.second_frame,textvariable=self.height).grid(row=24,column=1)
        Label(self.second_frame,text ='Meters').grid(row=24,column=2)
        Label(self.second_frame,text='Define Height of vehicle body. The resolution is 5cm. The value Range is 0,127',fg ='red',font= ('Aerial', 8)).grid(row=24,column=5,sticky =W)
        self.scale=Scale(self.second_frame,variable=self.height_range ,from_= 0 ,to=127, orient=HORIZONTAL,command=lambda e :self.height.set(float(e)*5/100)).grid(row=24, column=3)#Scale slider and function to convert the centimeters

        #Width
        self.label23 = Label(self.second_frame,text='Width').grid(row=25,column=0,padx=5,pady=5)
        self.entry23 = Entry(self.second_frame,textvariable=self.width).grid(row=25,column=1)
        self.scale=Scale(self.second_frame,variable=self.width_range ,from_= 0 ,to=1023, orient=HORIZONTAL,command=lambda e :self.width.set(float(e)*1/100)).grid(row=25, column=3) 
        Label(self.second_frame,text='Define Width of vehicle body.The resolution is 1 cm. The value Range is  0,1023',fg ='red',font= ('Aerial', 8)).grid(row=25,column=5,sticky =W)
        Label(self.second_frame,text ='Meters').grid(row=25,column=2)

        #Length
        self.label24 = Label(self.second_frame,text='length').grid(row=26,column=0,padx=5,pady=5)
        self.entry24 = Entry(self.second_frame,textvariable=self.length).grid(row=26,column=1)
        self.scale=Scale(self.second_frame,variable=self.length_range,from_= 0 ,to=4095, orient=HORIZONTAL,command=lambda e :self.length.set(float(e)*1/100)).grid(row=26, column=3) 
        Label(self.second_frame,text='Define Length of vehicle body.The resolution is 1 cm. The value Range is 0,4095 ',fg ='red',font= ('Aerial', 8)).grid(row=26,column=5,sticky =W)
        Label(self.second_frame,text ='Meters').grid(row=26,column=2)
        

class VehicleClassification(VehicleSize):

    def __init__(self):
        super().__init__()
        self.veh_class = IntVar()
        self.veh_class_entry =StringVar()
        self.fuel_type = IntVar()
        self.fuel_type_entry =IntVar()
        #Type of the Vehicle
        self.type_vehi =["Car","Bike","Bus","Truck"]
        self.label26   = Label(self.second_frame,text='Type of the vehcile').grid(row=28,column=0,padx=5,pady=5)
        self.combovehi = ttk.Combobox(self.second_frame,values= self.type_vehi)
        self.combovehi.set("Car")
        self.combovehi.bind("<<ComboboxSelected>>",self.selectedtype)
        self.entry26   = Entry(self.second_frame,textvariable=self.veh_class_entry).grid(row=28,column=2)
        self.combovehi.grid(row=28, column=1)

        #Fuel type
        self.fueltype_choice =["unknownFuel","gasoline","ethanol","diesel","electric","hybrid","hydrogen","natGasLiquid","natGasComp","propane"]
        self.label27   = Label(self.second_frame,text='Fuel Type').grid(row=29,column=0,padx=5,pady=5)
        Label(self.second_frame,text='Define the fuel power type of the vehicle.',fg ='red',font= ('Aerial', 8)).grid(row=29,column=5,sticky =W)
        self.entry27   = Entry(self.second_frame,textvariable=self.fuel_type_entry).grid(row=29,column=2)
        self.combofuel = ttk.Combobox(self.second_frame,values=self.fueltype_choice)
        self.combofuel.set("unknownFuel")
        self.combofuel.bind("<<ComboboxSelected>>",self.selectedfuel)

        self.combofuel.grid(row=29, column=1)
        Label(self.second_frame,text=' * Unknown Fuel - 0.\n Gasoline - 1.\n Ethanol - 2.\n Diesel - 3.\n Electric - 4.\n Hybrid - 5.\n Hydrogen - 6.\n Nat Gas Liquid - 7.\n Nat Gas Comp - 8.\n Propane - 9.',fg ='red',font= ('Aerial', 8)).grid(row=29,column=3,sticky =W)
    

    def selectedfuel(self,event):
        if self.combofuel.get() =="unknownFuel":
           self.fuel_type_entry.set(0)
        elif self.combofuel.get() =="gasoline":
           self.fuel_type_entry.set(1)
        elif self.combofuel.get() =="ethanol":
            self.fuel_type_entry.set(2)
        elif self.combofuel.get() =="diesel":
            self.fuel_type_entry.set(3)
        elif self.combofuel.get() =="electric":
            self.fuel_type_entry.set(4)
        elif self.combofuel.get() =="hybrid":
            self.fuel_type_entry.set(5)
        elif self.combofuel.get() =="hydrogen":
           self.fuel_type_entry.set(6)
        elif self.combofuel.get() =="natGasLiquid":
           self.fuel_type_entry.set(7)
        elif self.combofuel.get() =="natGasComp":
           self.fuel_type_entry.set(8)
        elif self.combofuel.get() =="propane":
           self.fuel_type_entry.set(9)
    
    def selectedtype(self,event):
        if self.combovehi.get() =="Car":
          self.veh_class_entry.set(0)
        elif self.combovehi.get() =="Bike":
           self.veh_class_entry.set(1)
        elif self.combovehi.get() =="Bus":
           self.veh_class_entry.set(2)
        elif self.combovehi.get() =="Truck":
            self.veh_class_entry.set(3)
       

#auxiliary information set for emergency vehicles or special vehicles. 
# It is used in BSM messages to inform the surrounding vehicles of the status of special operations of any
#emergency vehicle or special vechicle, remind them to give priority or keep clear.

class VehicleEmergencyExtension(VehicleClassification):

    def __init__(self):
        super().__init__()

        self.response_type = StringVar()
        self.response_type_entry =IntVar()
        self.lights_use = StringVar()
        self.lights_use_entry =IntVar()
        self.sirenuse =StringVar()
        self.sirenuse_entry=IntVar()
        self.unavailable=IntVar()


        #

        #Response Type
        self.responsetype_choice_one =["notInUseOrNotEquipped","emergency","nonEmergency","pursuit","stationary","slowMoving","stopAndGoMovement"]
        self.responsetype_choice_value=[0,1,2,3,4,5,6]
        self.label29  = Label(self.second_frame,text='Response Type').grid(row=31,column=0,padx=5,pady=5)
        self.entry29  = Entry(self.second_frame,textvariable=self.response_type_entry).grid(row=31,column=2)
        Label(self.second_frame,text='Define the current running state or driving behavior of emergency vehicles or special vehicles.',fg ='red',font= ('Aerial', 8)).grid(row=31,column=5,sticky =W)
        self.combo2 = ttk.Combobox(self.second_frame,values= self.responsetype_choice_one)
        self.combo2.bind("<<ComboboxSelected>>",self.selectedRes)
        self.combo2.set("Not In Use Or Not Equipped")
        self.combo2.grid(row=31, column=1)
        Label(self.second_frame,text=' * Not In Use Or Not Equipped - 0.\n Emergency- 1.\n Non Emergency - 2.\n Pursuit - 3.\n Stationary - 4.\n Slow Moving - 5.\n Stop And Go Movement - 6.',fg ='red',font= ('Aerial', 8)).grid(row=31,column=3)
    
        #Lightuse
        self.light_choice_one =["unavailable","notInUse","inUse","yellowCautionLights","schooldBusLights","arrowSignsActive","slowMovingVehicle","freqStops"]
        self.label30  = Label(self.second_frame,text='Lightbar In Use').grid(row=32,column=0,padx=5,pady=5)
        self.entry30  = Entry(self.second_frame,textvariable= self.lights_use_entry).grid(row=32,column=2)
        self.combo3 = ttk.Combobox(self.second_frame ,values=self.light_choice_one)
        self.combo3.bind("<<ComboboxSelected>>",self.selectedlight)
        self.combo3.set("unavailable")
        self.combo3.grid(row=32, column=1)
        Label(self.second_frame,text='Define the working status of warning lights or external display devices for emergency vehicles or special vehicles.',fg ='red',font= ('Aerial', 8)).grid(row=32,column=5,sticky =W)
        Label(self.second_frame,text=' * Unavailable - 0.\n Not In Use - 1.\n In Use - 2.\n Yellow Caution Lights - 3.\n Schoold Bus Lights - 4.\n arrow Signs Active - 5. \n slow Moving Vehicle - 6. \n freq Stops- 7',fg ='red',font= ('Aerial', 8)).grid(row=32,column=3,padx=2,pady=2)

        #Siren Use
        self.siren_choice =["unavailable","notInUse","inUse ","reserved"]
        self.label31 =Label(self.second_frame,text ='Siren Use').grid(row=33,column =0,padx=5,pady=5)
        self.entry31  = Entry(self.second_frame,textvariable= self.sirenuse_entry).grid(row=33,column=2)
        self.combo_siren = ttk.Combobox(self.second_frame,values= self.siren_choice)
        self.combo_siren.set("Unavailable")
        self.combo_siren.bind("<<ComboboxSelected>>",self.selectedSiren)
        self.combo_siren.grid(row=33, column=1)
        Label(self.second_frame,text='Define the status of sirens or any special sounding devices for emergency vehicles or special vehicles.',fg ='red',font= ('Aerial', 8)).grid(row=33,column=5,sticky =W)
      
        Label(self.second_frame,text=' * Unavailable - 0.\n notInUse- 1.\n inUse - 2.\n reserved- 3.',fg ='red',font= ('Aerial', 8)).grid(row=33,column=3,padx=2,pady=2)
    def selectedRes(self,event):
        if self.combo2.get() =="notInUseOrNotEquipped":
           self.response_type_entry.set(0)
        elif self.combo2.get() =="emergency":
            self.response_type_entry.set(1)
        elif self.combo2.get() =="nonEmergency":
            self.response_type_entry.set(2)
        elif self.combo2.get() =="pursuit":
            self.response_type_entry.set(3)
        elif self.combo2.get() =="stationary":
            self.response_type_entry.set(4)
        elif self.combo2.get() =="slowMoving":
            self.response_type_entry.set(5)
        elif self.combo2.get() =="stopAndGoMovement":
            self.response_type_entry.set(6)

    def selectedlight(self,event):
        if self.combo3.get() =="unavailable":
           self.lights_use_entry.set(0)
        elif self.combo3.get() =="notInUse":
            self.lights_use_entry.set(1)
        elif self.combo3.get() == "inUse":
            self.lights_use_entry.set(2)
        elif self.combo3.get() == "yellowCautionLights":
            self.lights_use_entry.set(3)
        elif self.combo3.get() =="schooldBusLights":
            self.lights_use_entry.set(4)
        elif self.combo3.get() =="arrowSignsActive":
            self.lights_use_entry.set(5)
        elif self.combo3.get() =="slowMovingVehicle":
            self.lights_use_entry.set(6)
        elif self.combo3.get() =="freqStops":
            self.lights_use_entry.set(7)
    def selectedSiren(self,event):
        if self.combo_siren .get() =="unavailable":
           self.sirenuse_entry.set(0)
        elif self.combo_siren .get() =="notInUse":
            self.sirenuse_entry.set(1)
        elif self.combo_siren .get() == "inUse":
            self.sirenuse_entry.set(2)
        elif self.combo_siren .get() == "reserved":
            self.sirenuse_entry.set(3)
      
     

class Events(VehicleEmergencyExtension):

    def __init__(self):
        super().__init__()
        self.events=StringVar()
        self.events_entry=IntVar()
        self.hazard_light = IntVar()
        self.ABS_activated = IntVar()
        self.Traction_loss =IntVar()
        self.Stability_control_activated =IntVar()
        self.Flat_tire =IntVar()
        self.Disable_vehicle = IntVar()
        self.Airbag_deployed =IntVar()

        #events
        self.events_choice =["None","eventHazardLights","eventStopLineViolation","eventABSactivated","eventTractionControlLoss","eventStabilityControlactivated","eventHazardousMaterials","eventReserved1","eventHardBraking","eventLightsChanged","eventWipersChanged","eventFlatTire","eventDisabledVehicle","eventAirBagDeployment"]
        self.comboevents = ttk.Combobox(self.second_frame,values= self.events_choice)
        self.comboevents.bind("<<ComboboxSelected>>",self.selectedEvents)
        self.comboevents.set("None")
        self.comboevents.grid(row=34, column=1)
        
        self.entry33  = Entry(self.second_frame,textvariable= self.events_entry).grid(row=34,column=2)
        
        Label(self.second_frame,text=' * None - 0.\n Hazard Light - 1.\n Stop Line Viloation - 2.\n ABS Activated - 3.\n Traction control loss - 4.\n Stability Control Activated - 5.\n Hazardous_Materials - 6.\n Reserved - 7.\n Hard Braking - 8.\n Lights Changed - 9.\n Wipers Changed - 10.\n Flat Tire - 11.\n Disable Vehicle - 12.\n Airbag deployed - 13',fg ='red',font= ('Aerial', 8)).grid(row=34,column=3,padx=2,pady=2)
        Label(self.second_frame,text=' * Vehicle special event ',fg ='red',font= ('Aerial', 8)).grid(row=34,column=5,padx=2,pady=2)

    def selectedEvents(self,event):
        if self.comboevents.get() =="None":
           self.events_entry.set(0)
        elif self.comboevents .get() =="eventHazardLights":
            self.events_entry.set(1)
        elif self.comboevents.get() == "eventStopLineViolation":
            self.events_entry.set(2)
        elif self.comboevents.get() == "eventABSactivated":
            self.events_entry.set(3)
        elif self.comboevents.get() =="eventTractionControlLoss":
            self.events_entry.set(4)
        elif self.comboevents.get() == "eventStabilityControlactivated":
            self.events_entry.set(5)
        elif self.comboevents.get() == "eventHazardousMaterials":
            self.events_entry.set(6)
        elif self.comboevents.get() == "eventReserved1":
            self.events_entry.set(7)
        elif self.comboevents.get() =="eventHardBraking":
            self.events_entry.set(8)
        elif self.comboevents.get() == "eventLightsChanged":
            self.events_entry.set(9)
        elif self.comboevents.get() == "eventWipersChanged":
            self.events_entry.set(10)
        elif self.comboevents.get() == "eventFlatTire":
            self.events_entry.set(11)
        elif self.comboevents.get() == "eventDisabledVehicle":
            self.events_entry.set(12)
        elif self.comboevents.get() == "eventAirBagDeployment":
            self.events_entry.set(13)
        
        
            
            
            
        

class Lights( Events):

    def __init__(self):
        super().__init__()
        self.lights =IntVar()
        self.lights_entry = StringVar()
        #self.lights_entry.set("All Lights")
        self.LIGHTS_ALL_LIGHTS_OFF = IntVar()
        self.LIGHTS_LOW_BEAM_HEAD_LIGHTS_ON  = IntVar() 
        self.LIGHTS_HIGH_BEAM_HEAD_LIGHTS_ON  = IntVar()
        self.LIGHTS_LEFT_TURN_SIGNAL_ON  = IntVar()
        self.LIGHTS_RIGHT_TURN_SIGNAL_ON  = IntVar()
        self.LIGHTS_HAZARD_SIGNAL_ON   = IntVar() 
        self.LIGHTS_AUTOMATIC_LIGHT_CONTROL_ON = IntVar()
        self.LIGHTS_DAYTIME_RUNNING_LIGHTS_ON    = IntVar()
        self.LIGHTS_FOG_LIGHT_ON  = IntVar()
        self.LIGHTS_PARKING_LIGHTS_ON  = IntVar()
        self.lights_choice =["All Lights","lowBeamHeadlightsOn","highBeamHeadlightsOn","leftTurnSignalOn","rightTurnSignalOn","hazardSignalOn","automaticLightControlOn","daytimeRunningLightsOn","fogLightOn","parkingLightsOn"]
        self.entry34    = Entry(self.second_frame,textvariable= self.lights).grid(row=35,column=2)
        self.combolights = ttk.Combobox(self.second_frame,values= self.lights_choice)
        self.combolights.bind("<<ComboboxSelected>>",self.selected_light)
        self.combolights.set("All Lights")
        self.combolights.grid(row=35, column=1)
    
        Label(self.second_frame,text=' * All lights off is indicated by no bits set .low Beam Headlights On - 0.\n high Beam Headlights On - 1.\n left Turn Signal On - 2.\n right Turn Signal On - 3.\n hazard Signal On - 4.\n automatic Light Control On - 5.\n daytime Running Lights On - 6.\n fog Light On - 7.\n parking Lights On - 8',fg ='red',font= ('Aerial', 8)).grid(row=35,column=3,padx=2,pady=2)
    def selected_light(self,event):
        if self.combolights.get() =="All Lights":
           self.lights.set(0)
        elif self.combolights .get() =="lowBeamHeadlightsOn":
            self.lights.set(0)
        elif self.combolights.get() =="highBeamHeadlightsOn":
            self.lights.set(1)
        elif self.combolights.get() == "leftTurnSignalOn":
            self.lights.set(2)
        elif self.combolights.get() =="rightTurnSignalOn":
            self.lights.set(3)
        elif self.combolights.get() == "hazardSignalOn":
            self.lights.set(4)
        elif self.combolights.get() == "automaticLightControlOn":
            self.lights.set(5)
        elif self.combolights.get() == "daytimeRunningLightsOn":
            self.lights.set(6)
        elif self.combolights.get() == "fogLightOn":
            self.lights.set(7)
        elif self.combolights.get() == "parkingLightsOn":
            self.lights.set(8)
       
class Position_Confidence(Lights):

    def __init__(self):
        super().__init__()
        self.pos_conf_pos =IntVar()
        self.pos_conf_ele = IntVar()

        self.options =['unavailable','500 m','200 m','100 m','50 m','20 m','10 m','5 m','2 m','1 m','0.50 m','0.20 m','0.10 m','0.05 m','0.02 m','0.01 m']


        #self.mycombo = ttk.Combobox(self.second_frame,self.clicked,*self.options)
        #Position Confidence
        self.label34 = Label(self.second_frame,text='Position Confidence').grid(row=36,column=0,padx=5,pady=5)
        self.entry34 = Entry(self.second_frame,textvariable= self.pos_conf_pos).grid(row=36,column=2)
        self.combo_pos = ttk.Combobox(self.second_frame,values= self.options)
        self.combo_pos.bind("<<ComboboxSelected>>",self.selected_pos)
        self.combo_pos.set("Unavailable")
        self.combo_pos.grid(row=36,column=1)
        Label(self.second_frame,text='Define the postional Confidence.The numerical value describes the vehicle position precision at 95% level.',fg ='red',font= ('Aerial', 8)).grid(row=36,column=5,sticky =W)
        Label(self.second_frame,text=' * Unavailable- 0.\n 500 m - 1.\n 200 m -2 .\n 100 m - 3.\n 50 m - 4.\n 20 m - 5.\n 10 m - 6.\n 5 m -7.\n 2 m - 8.\n 0.50 m - 9.\n 0.20 m - 10.\n 0.10 m - 11.\n 0.05 m -12 .\n 0.02 m -13.\n 0.01 -14',fg ='red',font= ('Aerial', 8)).grid(row=36,column=3,padx=2,pady=2)

        #Elevation Confidence
        self.options_elev =['Not Equipped or unavailable','500 m','200 m','100 m','50 m','20 m','10 m','5m','2 m','1 m','50 cm','20 cm','10 cm','5 cm','2 cm','1 cm']
        self.label35 = Label(self.second_frame,text='Elevation Confidence').grid(row=37,column=0,padx=5,pady=5)
        self.entry35 = Entry(self.second_frame,textvariable= self.pos_conf_ele).grid(row=37,column=2)
        self.combo_ele = ttk.Combobox(self.second_frame,values= self.options_elev)
        self.combo_ele.set("Unavailable")
        self.combo_ele.bind("<<ComboboxSelected>>",self.selected_ele)
        self.combo_ele.grid(row=37,column=1)
        Label(self.second_frame,text='Define elevation confidence. The numerical value describes the vehicle position precision at 95% level.',fg ='red',font= ('Aerial', 8)).grid(row=37,column=5,sticky =W)
        Label(self.second_frame,text=' * Unavailable- 0.\n 500 m - 1.\n 200 m -2 .\n 100 m - 3.\n 50 m - 4.\n 20 m - 5.\n 10 m - 6.\n 5 m -7.\n 2 m - 8.\n 1 m - 9.\n 0.20 m - 10.\n 0.10 m - 11.\n 0.05 m -12 .\n 0.02 m -13.\n 0.01 -14',fg ='red',font= ('Aerial', 8)).grid(row=37,column=3,padx=2,pady=2)

      
        Button(self.second_frame,text="SEND",command=self.sendData,font=('Helvetica', 10, 'bold'),height=3,width=15).grid(row=38,column=2,padx=15,pady=15)
        Button(self.second_frame,text="START",command=self.start_data,font=('Helvetica', 10, 'bold'),height=3,width=15).grid(row=38,column=3,padx=15,pady=15)
        Button(self.second_frame,text="STOP",command=self.stop_data,font=('Helvetica', 10, 'bold'),height=3,width=15).grid(row=38,column=4,padx=15,pady=15)
       

    def selected_pos(self,event):
        if self.combo_pos.get() =='unavailable':
           self.pos_conf_pos.set(0)
        elif self.combo_pos .get() =='500 m':
            self.pos_conf_pos.set(1)
        elif self.combo_pos.get() == '200 m':
            self.pos_conf_pos.set(2)
        elif self.combo_pos.get() == '100 m':
            self.pos_conf_pos.set(3)
        elif self.combo_pos.get() == '50 m':
            self.pos_conf_pos.set(4)
        elif self.combo_pos.get() == '20 m':
            self.pos_conf_pos.set(5)
        elif self.combo_pos.get() == '10 m':
            self.pos_conf_pos.set(6)
        elif self.combo_pos.get() == '5 m':
            self.pos_conf_pos.set(7)
        elif self.combo_pos.get() == '2 m':
            self.pos_conf_pos.set(8)
        elif self.combo_pos.get() == '1 m':
            self.pos_conf_pos.set(9)
        elif self.combo_pos.get() == '0.50 m':
            self.pos_conf_pos.set(10)
        elif self.combo_pos.get() == '0.20 m':
            self.pos_conf_pos.set(11)
        elif self.combo_pos.get() == '0.10 m':
            self.pos_conf_pos.set(12)
        elif self.combo_pos.get() =='0.05 m':
            self.pos_conf_pos.set(13)
        elif self.combo_pos.get() =='0.02 m':
           self.pos_conf_pos.set(14)
        elif self.combo_pos.get() =='0.01 m':
            self.pos_conf_pos.set(15)

    def selected_ele(self,event):
        if self.combo_ele.get() =='unavailable':
           self.pos_conf_ele.set(0)
        elif self.combo_ele .get() =='500 m':
            self.pos_conf_ele.set(1)
        elif self.combo_ele.get() == '200 m':
            self.pos_conf_ele.set(2)
        elif self.combo_ele.get() == '100 m':
            self.pos_conf_ele.set(3)
        elif self.combo_ele.get() == '50 m':
            self.pos_conf_ele.set(4)
        elif self.combo_ele.get() == '20 m':
            self.pos_conf_ele.set(5)
        elif self.combo_ele.get() == '10 m':
            self.pos_conf_ele.set(6)
        elif self.combo_ele.get() == '5 m':
            self.pos_conf_ele.set(7)
        elif self.combo_ele.get() == '2 m':
            self.pos_conf_ele.set(8)
        elif self.combo_ele.get() == '1 m':
           self.pos_conf_ele.set(9)
        elif self.combo_ele.get() == '50 cm':
            self.pos_conf_ele.set(10)
        elif self.combo_ele.get() == '20 cm':
           self.pos_conf_ele.set(11)
        elif self.combo_ele.get() == '10 cm':
            self.pos_conf_ele.set(12)
        elif self.combo_ele.get() ==' 5 cm':
            self.pos_conf_ele.set(13)
        elif self.combo_ele.get() ==' 2 cm':
           self.pos_conf_ele.set(14)
        elif self.combo_ele.get() ==' 1 cm':
            self.pos_conf_ele.set(15)


    def sendData(self):
        Hostflag = "{} = {}". format(self.comboflag.get(),self.host_flag.get())
        Msg_cnt_Value =self.msgCnt.get()#it stores the value from tkinter entry to Msg_cnt_Value
        id_value =self.id.get()
        Latitude=self.Lat.get()#it stores the value from tkinter entry to Latitude variable
        Longitude =self.long.get()
        Elevation =self.ele.get()
        semimajor = self.semimajor.get()
        semiminor =self.semiminor.get()
        semiorient =self.orient.get()
        Lateral_Acceleration = self.Acc_Lat.get()
        Longitudal_Acceleration =self.Acc_Lng.get()
        Vertical_Acceleration = self.Acc_Vert.get()
        Yaw_Rate =self.Yaw_rate.get()
        transmission_state= "{} = {}". format(self.combo1.get(),self.entryoptout.get())
        Vehicle_classification= "{} = {}". format(self.combovehi.get(),self.veh_class_entry.get())
        Vehicle_classification_type= "{} = {}". format(self.combofuel.get(),self.fuel_type_entry.get())
        Vehicle_emergency_ext="{} = {}".format(self.combo2.get(),self.response_type_entry.get(),self.lights_use_entry.get())
        Vehicle_emergency_ext_light="{} = {}".format(self.combo3.get(),self.lights_use_entry.get())
        Vehicle_emergency_ext_siren="{} = {}".format(self.combo_siren.get(),self.sirenuse_entry.get())
        Brake_system_status ="{} = {}".format(self.combobrake.get(),self.abs.get())
        events ="{} = {}".format(self.comboevents.get(),self.events_entry.get())
        light ="{} = {}".format(self.combolights.get(),self.lights.get())
        Position_confidence ="{} = {}".format(self.combo_pos.get(),self.pos_conf_pos.get())
        Elevation_confidence ="{} = {}".format(self.combo_ele.get(),self.pos_conf_ele.get())

        Heading =self.heading.get()
        Speed =self.speed.get()
        Angle = self.angle.get()
        Height = self.height.get()
        Width =self.width.get()
        Length =self.length.get()
       
    
       


        message = {}#Empty dict
       
        message["HostFlag"]=Hostflag
        message["MsgCount"]=Msg_cnt_Value # Accessing elements thorugh dictionary keys
        message["Id"] =id_value
        message["Latitude"]=Latitude # Accessing elements thorugh dictionary keys
        message["Longitude"] =Longitude 
        message["Elevation"] =Elevation
        message["SemiMajorAxisAccuracy"]=semimajor
        message["SemiMinorAxisAccuracy"]=semiminor
        message["SemiMajorAxisOrientation"]=semiorient
        message["LateralAcceleration"]=Lateral_Acceleration
        message["LongitudalAcceleration"]=Longitudal_Acceleration
        message["VerticalAcceleration"]= Vertical_Acceleration
        message["YawRate"]=Yaw_Rate
        message['TransmissionState']=transmission_state
        message["ResponseType"] = Vehicle_emergency_ext
        message["LightbarInUse"] = Vehicle_emergency_ext_light
        message["SirenInUse"] = Vehicle_emergency_ext_siren
        message["BrakeSystemStatus"]=Brake_system_status
        message["Events"] =events
        message["Light"] =light
        message["PostionConfidence"]=Position_confidence
        message["ElevationConfidence"]=Elevation_confidence
        message["BasicVehicleClass"]=Vehicle_classification
        message["FuelType"]=Vehicle_classification_type
        message["Heading"] =Heading
        message["Speed"] = Speed
        message['SteeringWheelAngle'] =Angle
        message["Height"]=Height
        message["Width"]=Width
        message["Length"] = Length
     
         #jsonMsg = json.dumps(message)
        #print(jsonMsg)
            #with open('BSM.json', 'w') as json_file:# converting dictionary to json format
                #json.dump(message, json_file)  
        # self.running=True
        msg = json.dumps(message)
        if self.running:
            print(msg)
            self.text = Text(self.second_frame,height = 10, width = 100,bg='black',fg='white')
            self.text.grid(row=39,column=3)
            self.text.insert(END,msg)
            udp_socket.sendto(msg.encode('utf-8'), dest_addr)
            print("Sending message to ROS driver")
            tkinter.messagebox.showinfo("Message","Sent Successfully") 

    def send_data(self):
    
        Hostflag = "{} = {}". format(self.comboflag.get(),self.host_flag.get())
        Msg_cnt_Value =self.msgCnt.get()#it stores the value from tkinter entry to Msg_cnt_Value
        id_value =self.id.get()
        Latitude=self.Lat.get()#it stores the value from tkinter entry to Latitude variable
        Longitude =self.long.get()
        Elevation =self.ele.get()
        semimajor = self.semimajor.get()
        semiminor =self.semiminor.get()
        semiorient =self.orient.get()
        Lateral_Acceleration = self.Acc_Lat.get()
        Longitudal_Acceleration =self.Acc_Lng.get()
        Vertical_Acceleration = self.Acc_Vert.get()
        Yaw_Rate =self.Yaw_rate.get()
        transmission_state= "{} = {}". format(self.combo1.get(),self.entryoptout.get())
        Vehicle_classification= "{} = {}". format(self.combovehi.get(),self.veh_class_entry.get())
        Vehicle_classification_type= "{} = {}". format(self.combofuel.get(),self.fuel_type_entry.get())
        Vehicle_emergency_ext="{} = {}".format(self.combo2.get(),self.response_type_entry.get(),self.lights_use_entry.get())
        Vehicle_emergency_ext_light="{} = {}".format(self.combo3.get(),self.lights_use_entry.get())
        Vehicle_emergency_ext_siren="{} = {}".format(self.combo_siren.get(),self.sirenuse_entry.get())
        Brake_system_status ="{} = {}".format(self.combobrake.get(),self.abs.get())
        events ="{} = {}".format(self.comboevents.get(),self.events_entry.get())
        light ="{} = {}".format(self.combolights.get(),self.lights.get())
        Position_confidence ="{} = {}".format(self.combo_pos.get(),self.pos_conf_pos.get())
        Elevation_confidence ="{} = {}".format(self.combo_ele.get(),self.pos_conf_ele.get())

        Heading =self.heading.get()
        Speed =self.speed.get()
        Angle = self.angle.get()
        Height = self.height.get()
        Width =self.width.get()
        Length =self.length.get()

        message = {}#Empty dict
       
        message["HostFlag"]=Hostflag
        message["MsgCount"]=Msg_cnt_Value # Accessing elements thorugh dictionary keys
        message["Id"] =id_value
        message["Latitude"]=Latitude # Accessing elements thorugh dictionary keys
        message["Longitude"] =Longitude 
        message["Elevation"] =Elevation
        message["SemiMajorAxisAccuracy"]=semimajor
        message["SemiMinorAxisAccuracy"]=semiminor
        message["SemiMajorAxisOrientation"]=semiorient
        message["LateralAcceleration"]=Lateral_Acceleration
        message["LongitudalAcceleration"]=Longitudal_Acceleration
        message["VerticalAcceleration"]= Vertical_Acceleration
        message["YawRate"]=Yaw_Rate
        message['TransmissionState']=transmission_state
        message["ResponseType"] = Vehicle_emergency_ext
        message["LightbarInUse"] = Vehicle_emergency_ext_light
        message["SirenInUse"] = Vehicle_emergency_ext_siren
        message["BrakeSystemStatus"]=Brake_system_status
        message["Events"] =events
        message["Light"] =light
        message["PostionConfidence"]=Position_confidence
        message["ElevationConfidence"]=Elevation_confidence
        message["BasicVehicleClass"]=Vehicle_classification
        message["FuelType "]=Vehicle_classification_type
        message["Heading"] =Heading
        message["Speed"] = Speed
        message['SteeringWheelAngle'] =Angle
        message["Height"]=Height
        message["Width"]=Width
        message["Length"] = Length
     
         #jsonMsg = json.dumps(message)
        #print(jsonMsg)
        with open('BSM.json', 'w') as json_file:# converting dictionary to json format
            json.dump(message, json_file)  
    
        msg = json.dumps(message)
        
        if self.running:
            #print(msg)
          
            self.text = Text(self.second_frame,height = 10, width = 100,bg='black',fg='white')
            self.text.grid(row=39,column=3)
            self.text.insert(END,msg)
            self.after(100,self.send_data)
            self.labelsent= Label(self.second_frame,text='Sending message to ROS driver over UDP in Json Format',fg='red')
            self.labelsent.grid(row=40,column=3)
            print("Sending message to ROS driver")
          
            udp_socket.sendto(msg.encode('utf-8'), dest_addr)
           
            #udp_socket.close()

    
       
    '''
    udp_socket.close()
    '''
    def start_data(self):
        #global running
        # if self.running == True:
        #     print(self.running)
        #     self.after(100,self.send_data) 
        self.running = True
        self.after(100,self.send_data)  
        
        #self.after(100,self.send_data) 
    def stop_data(self):
        self.running = False
        #print(self.running)
        self.after(100,self.send_data)
      
       
     
def main():
    #root = V2X_BSM()
    #root = Position()
    #root =AccelerationSet4way()
    #root =BrakeSystemStatus()
    #root =TransmissionState()
    #root =VehicleSize()
    #root =VehicleClassification()
    #root = VehicleEmergencyExtension()
    #root = Events()
    #root = Lights()
    #root=tk.Tk()
    root = Position_Confidence()
   # root.after(100)
    root.canvas.mainloop()
    
 
if __name__ == "__main__":
    main()




        
