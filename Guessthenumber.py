import random

secretnumber = random.randint(1,20)  #Picks a random number

print('Lets play a game!')
print('I want you to guess the number I am thinking of between 1 and 20')
print('You have 7 guesses.')
print('Ready?')
print('Begin!')

x = 0


while x < 7:
    guess = input()
    if int(guess) < secretnumber:
        print('Your guess is too low, try again.')
    elif int(guess) > secretnumber:
        print('Your number is too high, try again.')
    elif int(guess) == secretnumber:
        break
    x = x +1
if x >= 7:
    print('Congratulations, you lost dumbass!')
else:
    print('Congratulations you won!')

    
