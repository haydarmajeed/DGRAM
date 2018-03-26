# ********************#
# SERVER SIDE         #
# Filename: Server.py #
# NoFileTransfer      #
# ******************* #

import socket # importing the socket library
import time   # importing the time library to time the data transfer between client and the server

HOST = "localhost"    # using the localhost of the machine
PORT = 5454           # using available port
BUFFER = 1024         # using a buffer of 1024

print "Waiting for a client to connect"     #message will be printed to client

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #using the default Iv4 AF.INET and socket.DGRAM for UDP connection
s.bind ((HOST, PORT)) # binding the socket to the host & port

while True:           # Creating while loop to display data non-stop
    info, address = s.recvfrom(BUFFER)
    print info, address
    time.sleep(1)     # sending data (1) byte a time

