# guessing number using while if statement in python
import random

play_game='n'
while(play_game=='n'):
    answer=random.randint(1,50)
    try_number=input('Guess a number between 1 and 50:')
    try_number=int(try_number)
    counter=1

    while try_number!=answer:
        if try_number>answer:
            print('Your number is too large.')
        if try_number<answer:
            print('Your number is too small.')
        try_number=int(input('Guess a number between 1 and 50'))
        count=counter+1
    print('you got it') 
    play_game=input('continue')
    

