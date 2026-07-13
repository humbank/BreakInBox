import serial
import json

PORT = "/dev/ttyACM0"
BAUD = 115200

ser = serial.Serial(PORT, BAUD, timeout=1)

def send(cmd, id):
    msg = {
        "id": id,
        "cmd": cmd
    }
    ser.write((json.dumps(msg) + "\n").encode())

 
def read():
    while True:
        try:
            line = ser.readline().decode().strip()
            if line:
                return line
        except Exception as e:
            return "error"