# ********************#
# CLIENT SIDE         #
# FileName: client.py #
# NoFileTransfer      #
# ********************#


import socket
import time


HOST   = "localhost"
PORT   = 5454
BUFFER = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

repeat= 0
while True:
    COMM = str(repeat)
    repeat += 1
    s.sendto(COMM, (HOST, PORT))
    print "Data is being transmitted to the Server"
    time.sleep(1)    

