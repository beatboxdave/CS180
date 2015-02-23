import random

#Python changed raw_input to be just input() a while ago
#latest python will throw errors if it tries to run raw_input
#fixed this issue
forename = input("Please provide your first name: ")
surname = input("Please provide your surname: ")
print ("Hello " + forename + " " + surname + "!")

#this is just a little basic random number guessing game 
#added to test out github further
guessesTaken = 0


number = random.randint(1, 20)
print('Well, ' + forename + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.') # There are eight spaces in front of print.

    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + forename + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)