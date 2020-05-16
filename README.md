Treehouse Techdegree 
#Project-1
Number Guessing Game

This is the first program made while doing the Treehouse Python Techdegree course. 

The user will be prompted to input a number between 1-50. The goal is to guess the secret number using as few guesses as possible. When the correct number is entered, the user is told how many guesses they used and asked if they would like to try again. If yes, then the current high score will be displayed. 

The secret number is chosen at random. 

There is a couple of steps taken to make sure the user is staying within the range of 1-50; using integers; and when asked to retry answer either YES or NO. 

The program is broken down into a couple of functions. 

The main_game() function is doing most of the work, containing the while-loop that will run until the users guess = the answer. The user will be told if the guess is too low or too high, making it easier for the user to navigate. 

When the users guess = the answer, a new function, correct_answer(), will be called to congratulate the guest and inform of the number of tries. 

After the correct_answer() function is done, the main_game() will check if the last attempt beat the current high score before it ends. If so, the high score is updated. 

At last, the retry() function will run to prompt the user to retry. If yes the main_game() is run; if no, the game ends. 

The start_game() function contains a welcome message and runs the other functions. 