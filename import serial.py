import serial
port = '/dev/ttyACM0'
brate = 115200
ser = serial.Serial(port, brate)
while True :
    ch = input()
    if ch == 'stop' :
        ser.write(ch.encode())
        data = ser.readline()
        data = data.decode()[:len(data)-2]
        print(len(data))
        print(data)
        
    if ch == 'foward' :
        ser.write(ch.encode())  
        data = ser.readline()
        data = data.decode()[:len(data)-2]
        print(len(data))
        print(data)