#Import serial port, import string module, import pynmea2 library
import serial
import string
import pynmea2


while True:
        port="\dev\ttyAMA0"
        ser=serial.Serialport, 9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
        newdata=ser.readline()
        
        
        if newdata[0:6] == "$GPRMC":
                newmsg=pynmea2.parse(newdata)
                lat=newmsg.latitude
                lng=newmsg.longitude
                gps = "The Latitude is" + str(lat) + "and Longitude is" + str(lng)
                print(gps)
