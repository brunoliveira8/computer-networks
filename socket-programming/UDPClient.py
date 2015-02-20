''' UDPClient.py
usage: python UDPClient.py HOSTNAMEorIP PORT
Reads text from user, sends to server, and prints answer
Modified by Dale R. Thompson, 2/10/15
'''

import sys

# Import socket library
from socket import *

# Set hostname or IP address from command line
serverName = sys.argv[1]

# Set port number by converting argument string to integer
serverPort = int(sys.argv[2])

# Choose SOCK_DGRAM, which is UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get message from user
message = raw_input('Input lowercase sentence: ')

# Create UDP segment with message, hostname/IP, and port. Send it
clientSocket.sendto(message,(serverName, serverPort))

# Wait for segment from server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print modifiedMessage

clientSocket.close()

