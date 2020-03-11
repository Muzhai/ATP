# import packages gereral information
from datetime import date
from datetime import datetime
import time
import socket
import keyboard

# import packages kamera
import cv2
from pyzbar import pyzbar
import imutils
from imutils.video import VideoStream
import time

# import packages gps
import serial
import time

from funktion import main
from funktion import query_table
from funktion import insert_table_batch
from funktion import query_table_id
from funktion import delete_table_id
from funktion import query_table_ele
from funktion import gps_map_marker



mssql = main()

breakout_command = 'e'                          # ends collecting infomation and sends the information to the database
device_id = socket.gethostname()                # default device id
reader_connected = True                         # If reader is connected variable set True


information_list = []                           # Create a list where information can be stored
data_list = 3
data_qr = {}
data_rfid = {}
vs = VideoStream( usePiCamera = True ).start()

def get_gps_location():

    # Enable Serial Communication
    port = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=1)
    # Transmitting AT Commands to the Modem
    # '\r\n' indicates the Enter key

    time.sleep(.01)

    # Activate Command line
    port.write("AT \r\n" .encode('utf-8'))
    rcv = port.read(100).decode()
    #print(rcv)
    time.sleep(.01)

    # Power On the gps module
    port.write("AT+CGNSPWR=1 \r\n" .encode('utf-8'))
    rcv = port.read(100).decode()
    #print(rcv)
    time.sleep(.01)

    #Set the baud rate of GPS
    port.write("AT+CGNSIPR=115200 \r\n" .encode('utf-8'))
    rcv = port.read(100).decode()
    #print(rcv)
    time.sleep(.10)

    #Check, if the gps signal is sufficiant
    chk = False
    search_for = '3D'
    while chk == False:
    
        port.write("AT+CGPSSTATUS? \r\n" .encode('utf-8'))
        rcv = port.read(100).decode()
        print(rcv)
        
        is_in = search_for in rcv
        if is_in == True:
            chk = True
            break

    #print(chk)    
    #print(rcv)


    #Send Data received to UART
    port.write("AT+CGNSTST=1 \r\n" .encode('utf-8'))
    #rcv = port.read(100).decode()
    #print(rcv)
    time.sleep(2.5)

    port.write("AT+CGNSTST=0 \r\n" .encode('utf-8'))


    #Print the GPS information
    port.write("AT+CGNSINF \r\n" .encode('utf-8'))
    rcv += port.read(200).decode()
    print(rcv)
    time.sleep(.1)


    #split data into a list
    data_raw = rcv.split(',')
    #print(data_raw)

    #search the list after N and E and get the index of the location
    index_N = data_raw.index('N')
    north_str = data_raw[index_N - 1]
    north_float = float(north_str)/100

    index_E = data_raw.index('E')
    east_str = data_raw[index_E - 1]
    east_float = float(east_str)/100

    #get the altitute and the salelites infomation
    location_N = str(north_float)
    location_E = str(east_float)
    altitude = str(data_raw[9])
    satelites = str(data_raw[7])
    print('location: ' + location_N + ', ' + location_E +', altitude: ' +altitude+ ', satelites: ' + satelites)
    data_list = location_N + ', '+location_E + ', '+ altitude +', '+ satelites
    #print('data_list_gps = '+data_list)
   


    #Stopp sending Data received to UART
    port.write("AT+CGNSTST=0 \r\n" .encode('utf-8'))
    #rcv = port.read(100).decode()
    #print(rcv)
    #time.sleep(.5)
    return data_list

def read_qr_codes(data_list):
    
        # initialize video stream and wait
        #vs = VideoStream( usePiCamera = True ).start()
        time.sleep(2.0)
        # loop over frames
        print('Scanning QR Codes')
        while True:
            frame = vs.read()
            # for better performance, resize the image
            frame = imutils.resize(frame, width=400)
            # find and decode all barcodes in this frame
            barcodes = pyzbar.decode(frame)
            #print('data_list_qr = '+data_list)
            for barcode in barcodes:
                #do anything with that data
                print('Code \"' + barcode.data.decode("utf-8") + '\" detected')
                tag_id_qr = barcode.data.decode("utf-8")    
                id_qr = {
                'tag_id' : str(tag_id_qr),
                'device_id' : str(device_id),
                'date' : str(time.strftime("%Y.%m.%d %H:%M:%S")),
                'GPS' : data_list
                }

                #data_qr.update(id_qr)
                information_list.append(id_qr)
                #information_list.append(data_list)
            if keyboard.is_pressed('ESC'):
                break
            
def read_rfid_codes(data_list):
    while reader_connected == True:                 # Check if reader is connected
        tag_id_rfid = input('Receive id from tag')       # Input is expected
        if (tag_id_rfid == breakout_command):
            break
        #print('data_list_rfid = '+data_list)
        id_rfid = {
           'tag_id' : str(tag_id_rfid),
           'device_id' : str(device_id),
           'date' : str(time.strftime("%Y.%m.%d %H:%M:%S")),
          # 'GPS' : data_list
           'GPS' : data_list
        }
        #data_rfid.update(id_rfid)
        information_list.append(id_rfid)
        #information_list.append(data_list)
        #print(information_list)            


def start_Program():
    try:
        while True:
            data_list = get_gps_location()
            #print('data_list_start_Program = '+data_list)
            read_qr_codes(data_list)
            read_rfid_codes(data_list)

            information_list_cleared = []
            for e in information_list:
                if e not in information_list_cleared:
                    information_list_cleared.append(e)

            print(information_list_cleared)
            #That would be the point when the information are either sent to the database or saved in a general list
        
            insert_table_batch(information_list_cleared)
        
            if keyboard.is_pressed('CTRL+ESC'):
                break
    except KeyboardInterrupt:
        pass
    #return information_list_cleared

start_Program()