import serial
import time
import random

def write_serial(data):
    bytes_written = ser.write(bytes(data, 'utf-8'))
    time.sleep(0.05)
    return bytes_written

def make_cocktail(durations):
    data = str(durations[0])
    for i in range(1,len(durations)):
        data += "|"+str(durations[i])
    print("Message")
    print(data)
    return write_serial(data)

def cancel_cocktail():
    write_serial("x")

cocktail = [random.randint(30,300) for i in range(6)]
flowrates = [random.randint(15,30) for i in range(6)]

for i in range(6):
    if random.randint(0,1) < 1:
        cocktail[i] = 0

durations = []
for i in range(6):
    durations.append(int(cocktail[i]/flowrates[i]*1000))

print("Cocktail")
print(cocktail)
print("Flowrates")
print(flowrates)
print("Duration")
print(durations)

ser = serial.Serial('COM6',115200,timeout=1)
if "RDY" in str(ser.readline()):
    make_cocktail(durations)

ser.close()