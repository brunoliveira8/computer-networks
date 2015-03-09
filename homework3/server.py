'''=============================================================================
 |    File Name:  server.py
 |
 |       Author:  Tarcisio Bruno Carneiro Oliveira
 |     Language:  Python 2.7
 |       To Run:  python server.py
 |
 |        Class:  CSCE4753
 |      Project:  HANGMAN
 |   Assumption:  [any prerequisite or precondition that must be met]
 | Date Created:  2-27-2015
 |    
 |
 +==========================================================================='''

import sys

# Import socket library
from socket import *

# Set port number by converting argument string to integer
serverPort = 5555

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

#HANGMAN VARIABLES
secretWord = "ARKANSAS"
hangWord = [" ", "H", "HA", "HAN", "HANG", "HANGM", "HANGMA", "HANGMAN"];
letters = {"A": "_", "R": "_","K": "_","N": "_","S": "_"}
guessedLetters = []
guessedLetters_msg = ''
guessed_letter = False
word = '{0} {1} {2} {0} {3} {4} {0} {4}'.format(letters["A"],letters["R"],letters["K"],letters["N"],letters["S"])
countMistakes = 0
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

      #this variable verifies if the user has already type the letter to send a warning
      guessed_letter = False

      #Verifies if the user tried to guess the all word.
      if len(sentence) >= 8:
        if capitalizedSentence == secretWord:
          result = "You won!"
          
          for key in letters.keys():
            letters[key] = key   
            word = '{0} {1} {2} {0} {3} {4} {0} {4}'.format(letters["A"],letters["R"],letters["K"],letters["N"],letters["S"])
                 
        else:
          result = "You lost!"
          countMistakes = 7

      else:
          #Verifies if the first characther sent is in the secretWord string.
          if secretWord.find(capitalizedSentence[0]) == -1:
              
              if capitalizedSentence[0] not in guessedLetters:         
                countMistakes = countMistakes + 1
                guessedLetters.append(capitalizedSentence[0])
                guessedLetters_msg = '-'.join(guessedLetters)
             
              else:
                guessed_letter = True

          #Change the dash for the right letter
          else:
            letters[capitalizedSentence] = capitalizedSentence
            word = '{0} {1} {2} {0} {3} {4} {0} {4}'.format(letters["A"],letters["R"],letters["K"],letters["N"],letters["S"])

          #Verifies if the user right all letters, and change the result
          if "_" not in letters.values():
            result = "You won!"

          #If the user have guessed for seven times, he lost
          elif countMistakes == 7:
            result = "You lost!"
          else:
            result = "Game continues"

      #format the message to send to the client
      if guessed_letter:
        message = 'You already tried this letter!\nNumber of wrong guess: {0} \nSecret Word: {1} \nGuessed letters: {2} \n{3}'.format(hangWord[countMistakes], word, guessedLetters_msg ,result)
      else:
        message = 'Number of wrong guess: {0}\nSecret Word: {1} \nGuessed letters: {2} \n{3}'.format(hangWord[countMistakes], word, guessedLetters_msg ,result)
      
      # Send it into established connection
      connectionSocket.send(message)
  
  # Close connection to client but do not close welcome socket 
  connectionSocket.close()

  #Overwrite the variables to start a new game
  hangWord = [" ", "H", "HA", "HAN", "HANG", "HANGM", "HANGMA", "HANGMAN"];
  guessedLetters = []
  guessedLetters_msg = ''
  guessed_letter = False
  letters = {"A": "_", "R": "_","K": "_","N": "_","S": "_"}
  word = '{0} {1} {2} {0} {3} {4} {0} {4}'.format(letters["A"],letters["R"],letters["K"],letters["N"],letters["S"])
  countMistakes = 0
  result = 'Game continues'

serverSocket.close()




