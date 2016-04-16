
'''=============================================================================
 |    File Name:  client.py
 |
 |       Author:  Tarcisio Bruno Carneiro Oliveira
 |     Language:  Python 2.7
 |   	 To Run:  python client.py
 |
 |        Class:  CSCE4753
 |      Project:  HANGMAN
 |   Assumption:  [any prerequisite or precondition that must be met]
 | Date Created:  2-27-2015
 |    
 |
 +==========================================================================='''

import sys
import time


# Import socket library
from socket import *

# Set hostname or IP address from command line
#serverName = sys.argv[1]
serverName = 'localhost'

# Set port number by converting argument string to integer
serverPort = 5555


# Choose SOCK_STREAM, which is TCP
clientSocket = socket(AF_INET, SOCK_STREAM)


# Connect to server using hostname/IP and port
clientSocket.connect((serverName, serverPort))

print "Let's play HANGMAN!"


while 1:

	#This wait guaraantes synchronization. It does not allow the user to send information so fast.
	time.sleep(0.05)

	# Get sentence from user
	sentence = raw_input('Guess a letter: ')
	while(len(sentence) == 0): 
		print 'Type a valid characther'
		sentence = raw_input('Input lowercase sentence: ')
		

	# Send it into socket to server
	clientSocket.send(sentence)

	# Receive response from server via socket
	modifiedSentence = clientSocket.recv(1024)

	print '\n------------------------------------------------------------------------'
	print 'From Server: '
	print modifiedSentence

	#The client program runs until the server send You win or You lost.
	if modifiedSentence.find('Game continues') == -1:
		break

clientSocket.close()



