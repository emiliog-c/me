"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!

    def lowerFunc():
      lowerBound = input("Smallest number of the range: ")
      while not lowerBound.isdigit():
        lowerBound = int(input("Please Input a number: "))
        return lowerBound
      return lowerBound
      

    def higherFunc():
      higherBound = input("Highest Number of the range: ")
      while not higherBound.isdigit():
        higherBound = int(input("Please Input a number: "))
        return higherBound
      return higherBound
      

    def fullFunc():
      tf = False
      lowz = lowerFunc()
      highz = higherFunc()
      realNum = random.randint(int(lowz), int(highz))
      while tf != True:
        guess = int(input("Guess a number between: " + (lowz) + " and " + (highz) + " "))
        print("You guessed {}".format(guess))
        if guess == realNum:
          print ("You got it!")
          tf = True
        elif guess < realNum:
          print ("Too small")
        else:
          print ("Too large")
      return "You got it!"



if __name__ == "__main__":
    print(advancedGuessingGame())
