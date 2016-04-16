
  =============================================================================
 |    File Names:  server.py and client.py
 |
 |       Author:  Tarcisio Bruno Carneiro Oliveira
 |     Language:  Python 2.7
 |   	 To Run:  1) python server.py
 |				  2) python client.py
 |				  Note: The server runs in localhost at the port 5555. 
 |				  The client has the this port and this hostname set as default.
 |
 |        Class:  CSCE4753
 |      Project:  HANGMAN
 |   Assumption:  The server.py runs first than client.py. 
 |				The port 5555 is not beeing user by another process.
 | Date Created:  2-27-2015
 |    
 |
 +==================================================================================================================================

1. General Functionality:

1.1 A TCP connection is opened between client and server, then the game starts.

1.2 The client sends a letter or a full world(8 letters or more) to the server.
  		If the client sends a string with the size less than 8, only the first character is assessed.

1.3 The server processing the information and sends a string with four lines and sometimes five when the user types a repeated letter.
		The first line represents the number of guesses represented by the word HANGMAN.
		The second line shows the secret word represented by dashes: _ _ _ _ _ _ _ _ 
		The third line shows the guessed letters.
		The fourth line shows the result: You won, you win or game continues.

1.4 When the game ends, the connection is closed and the server waits for another connection.

+=====================================================================================================================================

2. How the requirements are implemented: 

 The user must be able to do the following from the client software:
a. See the number of letters in the word
	Each wrong guess, a letter from the word HANGMAN is added to the first line that starts as a blank line.

b. Guess letters.
	The third line shows a list of guessed letters.

c. See the position of correct letters in the word.
	Each right answer, the string _ _ _ _ _ _ _ showed in the second line is changed. For example, if the user has typed 'A', the string is A _ _ A _ _ A _

d. Be told when the user loses and display the word.
	The last line show a message saying 'You won', 'You lost' or 'Games Continues'

e. Be told when the user wins.
	The last line show a message saying 'You won', 'You lost' or 'Games Continues'


