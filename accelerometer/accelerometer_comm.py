import serial
import time

COM_PORT = 'COM10'
BAUD_RATE = 9600
TIMEOUT = 0
                      
def getRollPitch(COM_PORT, BAUD_RATE=9600, TIMEOUT=0):  

    # (Potentially) Replace COM Port used on Arduino and Baud Rate
    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout = TIMEOUT)
    temp = 0
    time.sleep(.3) 

    # Initial reading of serial monitor
    val = ser.readline() 

    # Loop until a complete line is returned, with 2 elements
    while not '\\n' in str(val) or not 'b' in str(val) and temp != 2:
        time.sleep(.3)                  
        val = ser.readline()  
        temp = len(val.decode().strip().split())
        print(temp)

    # Decode, strip unecessary characters
    val = val.decode().strip()   
    # Split into roll and pitch values
    val = val.split()

    # Access and define roll and pitch
    roll = val[0]
    pitch = val [1]

    return roll, pitch


r, p = getRollPitch(COM_PORT)
print(f'Roll {r} Pitch {p}')


