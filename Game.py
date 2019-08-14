import random

numberofGuesses = 0
number = random.randint(1,100) # This generates a random number between 1-100

name = input("Hello, What is your name? ")
print(name + ", I am thinking of a whole number between 1 and 100. Can you guess what it is?, in 10 guesses")

while numberofGuesses < 10:
  guess = input("Take a guess, my friend:") # this is where the user starts to guess the number 
  guess = int(guess)

  numberofGuesses = numberofGuesses + 1;
  guessesLeft = 10 - numberofGuesses;

  if guess < number:
    guessesLeft=str(guessesLeft)
    print("Your guess is too low! You still have " + guessesLeft + " guesses left, My friend") # this tells the user that the number is too low

  if guess > number:
    guessesLeft=str(guessesLeft)
    print("Your guess is too high! bud You still have " + guessesLeft + " guesses left, My friend") # this tell the user that the number is to high 

  if guess==number:
    break

if guess==number:
  numberofGuesses=str(numberofGuesses)
  print("Great job! my friend, You guessed the number in " + numberofGuesses + " tries ") # thus tells the user that they have guessed the number correct 

if guess!=number:
  number=str(number)
  print("Sorry Dude, The number I was thinking of was " + number + " :)") # this tells the user that the have run out of guesses and tells them what the number was
  
input("press Enter to Exit")

