''' UDPServer.py
usage: python UDPServer.py PORT
Reads in text, changes all letters to uppercase, and returns
the text to the client
Modified by Dale R. Thompson, 2/10/15
'''

import sys

# Import socket library
from socket import *

# Set port number by converting argument string to integer
serverPort = int(sys.argv[1])

# Choose SOCK_DGRAM, which is UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Start listening on specified port
serverSocket.bind(('', serverPort))

print "The server is ready to receive"

# Forever, read in sentence, convert to uppercase, and send
while 1:
  # Return data and address
  message, clientAddress = serverSocket.recvfrom(2048)

  # Converts to uppercase
  modifiedMessage = message.upper()

  # Send modified message back to client
  serverSocket.sendto(modifiedMessage, clientAddress)
