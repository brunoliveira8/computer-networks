''' server.py
usage: python TCPServer.py PORT
Reads in text, changes all letters to uppercase, and returns
the text to the client
Modified by Dale R. Thompson, 2/10/15
'''

import sys

# Import socket library
from socket import *

# Set port number by converting argument string to integer
#serverPort = int(sys.argv[1])
serverPort = 7081

# Choose SOCK_STREAM, which is TCP
# This is a welcome socket
try:
    #create an AF_INET, STREAM socket (TCP)
    serverSocket = socket(AF_INET, SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit();


# Start listening on specified port
serverSocket.bind(('', serverPort))

# Listener begins listening
serverSocket.listen(1)

#HANGMAN VARIABLE
secretWord = "ARKANSAS"
hangWord = ["H", "HA", "HAN", "HANG", "HANGM", "HANGMA", "HANGMAN", " "];
letters = {"A": "_", "R": "_","K": "_","N": "_","S": "_"}
word = '{0} {1} {2} {0} {3} {4} {0} {4}'.format(letters["A"],letters["R"],letters["K"],letters["N"],letters["S"])
countMistakes = -1
result = 'Game continues'

print "The server is ready to receive"

# Forever, read in sentence, convert to uppercase, and send
while 1:


  # Wait for connection and create a new socket
  # It blocks here waiting for connection
  connectionSocket, addr = serverSocket.accept()
 
  while result == 'Game continues':
      # Read bytes from socket
      sentence = connectionSocket.recv(1024)

      # Convert sentence to uppercase
      capitalizedSentence = sentence.upper()

      if len(sentence) >= 8:
        if capitalizedSentence == secretWord:
          result = "You won!"
          for key in letters.keys():
            letters[key] = key   
            word = '{0} {1} {2} {0} {3} {4} {0} {4}'.format(letters["A"],letters["R"],letters["K"],letters["N"],letters["S"])
            if countMistakes == -1:
              countMistakes = 7       
        else:
          result = "You lost!"
          countMistakes = 6


      else:
          if secretWord.find(capitalizedSentence[0]) == -1:
            countMistakes = countMistakes + 1
            print countMistakes
          else:
            letters[capitalizedSentence] = capitalizedSentence
            word = '{0} {1} {2} {0} {3} {4} {0} {4}'.format(letters["A"],letters["R"],letters["K"],letters["N"],letters["S"])

          if "_" not in letters.values():
            result = "You won!"

          elif countMistakes == 6:
            result = "You lost!"
          else:
            result = "Game continues"

      message = '{0} \n{1} \n{2}'.format(hangWord[countMistakes], word, result)
      
      # Send it into established connection
      connectionSocket.send(message)
  
  # Close connection to client but do not close welcome socket 

  connectionSocket.close()
  hangWord = ["H", "HA", "HAN", "HANG", "HANGM", "HANGMA", "HANGMAN"];
  letters = {"A": "_", "R": "_","K": "_","N": "_","S": "_"}
  word = '{0} {1} {2} {0} {3} {4} {0} {4}'.format(letters["A"],letters["R"],letters["K"],letters["N"],letters["S"])
  countMistakes = -1
  result = 'Game continues'

serverSocket.close()




