# Interactive Guess the Number Game 

"""
Challenge 1
    The computer will think of a random number from 1 to 10 as secret number
"""


"""
    Then ask you ( Player ) to guess the number and store as guess number
"""



"""



    Compare the guess number with the secret number 
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""
import random

MAX_TRIES = 6
guessCount = 0

while (guessCount < MAX_TRIES):
  secret_number = random.randint(1,10)
  guess = input("Guess the number between 1 and 10: ")

  if not guess:
    guessCount = guessCount + 1
    print ("No guess given, try again")
    #break
    continue

  guess = int(guess)

  if (guess == secret_number):
    print ("Player wins, computer loses")
    break
  else:
    guessCount = guessCount + 1
    print ("Player loses and computer wins")
    print ("Tries Left:", MAX_TRIES - guessCount)
    if (guess < secret_number):
      print ("Player guessed LOW")
    elif (guess > secret_number):
      print ("Player guessed HIGH")
  
