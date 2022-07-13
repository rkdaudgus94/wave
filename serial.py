import serial
port = '/dev/ttyACM0'
brate = 115200
ser = serial.Serial(port, brate)
try:
    while True :
        ch = input()
        if ch == 's' :
            ser.write('stop'.encode())
            data = ser.readline()
            data = data.decode()[:len(data)-2]
            print(len(data))
            print(data)
            
        if ch == 'f' :
            ser.write('front'.encode())  
            data = ser.readline()
            data = data.decode()[:len(data)-2]
            print(len(data))
            print(data)

except KeyboardInterrupt :
    pass