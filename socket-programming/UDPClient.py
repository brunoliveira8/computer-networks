from socket import *

serverName = "turing.uark.edu"

serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = raw_input("Input lowercase sentence: ")

clientSocket.sendto(message, (serverName, serverPort))

modifiedMessage, serverAdress = clientSocket.recvfrom(2048)

print modifiedMessage

clientSocket.close()

