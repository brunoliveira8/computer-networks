''' client.py
usage: python TCPClient.py HOSTNAMEorIP PORT
Reads text from user, sends to server, and prints answer
Modified by Dale R. Thompson, 2/10/15
'''

import sys

# Import socket library
from socket import *

# Set hostname or IP address from command line
#serverName = sys.argv[1]
serverName = 'localhost'

# Set port number by converting argument string to integer
#serverPort = int(sys.argv[2])
serverPort = 7087
# Choose SOCK_STREAM, which is TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect to server using hostname/IP and port
clientSocket.connect((serverName, serverPort))

# Get sentence from user
sentence = raw_input('Input lowercase sentence: ')

# Send it into socket to server
clientSocket.send(sentence)

# Receive response from server via socket
modifiedSentence = clientSocket.recv(1024)

print 'From Server: ', modifiedSentence

clientSocket.close()
