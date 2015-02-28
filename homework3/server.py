''' TCPServer.py
usage: python TCPServer.py PORT
Reads in text, changes all letters to uppercase, and returns
the text to the client
Modified by Dale R. Thompson, 2/10/15
'''

import sys

# Import socket library
from socket import *

# Set port number by converting argument string to integer
serverPort = int(sys.argv[1])

# Choose SOCK_STREAM, which is TCP
# This is a welcome socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Start listening on specified port
serverSocket.bind(('', serverPort))

# Listener begins listening
serverSocket.listen(1)

print "The server is ready to receive"

# Forever, read in sentence, convert to uppercase, and send
while 1:
  # Wait for connection and create a new socket
  # It blocks here waiting for connection
  connectionSocket, addr = serverSocket.accept()

  # Read bytes from socket
  sentence = connectionSocket.recv(1024)
  
  # Convert sentence to uppercase
  capitalizedSentence = sentence.upper()
  
  # Send it into established connection
  connectionSocket.send(capitalizedSentence)
  
  # Close connection to client but do not close welcome socket
  connectionSocket.close()
