"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


high_score = 51


def correct_answer(number_of_tries):
  
  if number_of_tries == 1:
    print("You got it on the first attempt. Excellent performance!\n")
  
  else: 
    print("You got it on {} tries. Well done!\n".format(number_of_tries)) 


def retry():
  
  play_again = ""

  while play_again != "YES" or play_again != "NO":

    play_again = input("Would you like to play again? YES / NO:  ")

    if play_again.upper() == "YES":
      main_game()

    elif play_again.upper() == "NO":
      print("\nThe game is over. Thank you for playing!")
      exit()  
      
    else:
      print("Please enter YES or NO!\n")

      
def main_game():
  
  global high_score
  answer = random.randint(1, 50)
  user_guess = 0
  guess_count = 0
  
  if high_score <= 50:
    print("\n--------> The current high score is {} guesses <--------\n".format(high_score))

  while user_guess != answer:
    
    try:
      user_guess = input("Guess a number from 1-50: ")
      user_guess = int(user_guess)
      guess_count += 1
    
    except ValueError: 
      print("Please enter an integer from 1-50!\n")
      continue
    
    else:
      if user_guess > 50:
        print("You chose a value that is not within the range of numbers for this game.\n")
        
      elif user_guess < answer:
        print("Too low. Try again!\n")
        
      elif user_guess > answer:
        print("Too high. Try again!\n")
      
      else:
        correct_answer(guess_count)
  
  if high_score > guess_count:
    high_score = guess_count
       

def start_game():
  
  print("\n--------> Welcome to The Number Guessing Game! <--------\n")
    
  main_game()
  
  retry()
                
start_game()