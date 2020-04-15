# THis is a guess the number game 
import random

guessestaken = 0

print("Hello, what is your name?")
myName = input()

number = random.randint(1,20)
print( 'Ok, ' + myName + ' I am thinking of a number between 1 and 20' )

for guessestaken in range(6):
    print('Have a guess')
    guess = input() #takes in the guess
    guess = int(guess) # converts to an integer

    if guess < number:
        print('your guess is too low')
    
    if guess > number:
        print("your guess is too high")

    if guess == number:
        break

if guess == number:
        guessestaken = str(guessestaken + 1)
        number = str(number)
        print('Well done! ' + myName + '. '+ number + ' was the correct number')
        print ('It took you '+ guessestaken + ' attempt(s) to guess this time')
    
if guess != number:
    number = str(number)
    print(' I am afraid that the number I was thinking of was ' + number)
    print('Better luck next time')

    