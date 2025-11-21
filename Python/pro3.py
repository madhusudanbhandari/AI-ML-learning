#rock paper scissor game

import random
choices=('r','p','s')
comp_choice=random.choice(choices)

while True:
    user_choice=input('Enter your choice (r/p/s): ')
    if user_choice not in choices:
        print('invalid choice')
        continue


    print(f'you choose '+user_choice)
    print(f'Computer choose '+ comp_choice)

    if (
        (user_choice=='p' and comp_choice=='r') or
        (user_choice=='s' and comp_choice=='p') or 
        (user_choice=='r' and comp_choice=='s')) :
         print('You win')

    else:
        print('You loose')


    reply=input('Do you want to continue: (y/n) ')
    if(reply=='n'):
        break