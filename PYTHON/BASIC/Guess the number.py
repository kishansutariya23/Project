import random
generated = (random.randint(1, 99))

def input_number(guess):

    while generated != guess:
        if guess > generated:
            print('your number is HIGH  ')
            guess =int(input('enter a number in range of 1 to 99:-'))
        elif guess<generated:
            print('your number is LOW')
            guess = int(input('enter a number in range of 1 to 99:-'))
        elif guess==generated:
            pass
        print('you Guess is correct')
        print('Wanna Play one more time?')
        yes= ['YES', 'yes', 'Yes']
        enter=input()
        if enter in yes:
            guess = int(input('enter a number in range of 1 to 99:-'))
        else:
            print('Thank you for playing')
            break

guess = int(input('enter a number in range of 1 to 99:-'))

input_number(guess)

