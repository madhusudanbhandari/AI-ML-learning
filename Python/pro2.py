
import random
num=random.randint(1,100)
while(True):
   try:
     guess=int(input('guess a number between 1 and 100: '))
    
     if(num<guess):
        print('lower')

     elif(num>guess):
        print('higher')

     else:
        print('correct guess')
        break
    
   except ValueError:
    print('Please enter a valid number')