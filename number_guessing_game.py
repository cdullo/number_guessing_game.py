import random

print("Greetings! Welcome to the Number Guessing Game!")

def start_game():
  number = random.randint(1, 51)
  attempts = 0
  while True:
    try:
      guess = int(input("Guess a number between 1 and 50: "))
      break
    except ValueError:
      print("Please enter an integer")
      continue
    else:
      break

  while guess != number:
    if guess > number:
      print("It's lower")
      guess = int(input("Try again: "))
      attempts += 1
    elif guess < number:
      print("It's higher")
      guess = int(input("Try again: "))
      attempts += 1
    else:
      break
    
    if guess == number:
      print("You got it!")
      print('It took you ' + str(attempts) + ' attempts to guess the number.')
      play_again = input('Play again? Enter "yes or no" ')
      if play_again == "y" or play_again == "yes" or play_again == "YES" or play_again == "Yes":
        start_game()
      else:
        print("Thanks for playing! Bye.")

start_game()
