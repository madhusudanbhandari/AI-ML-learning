import random
count=0
while (True):
    choice=input('Roll a dice! (y/n): ').lower()

    if(choice=='y'):
        val1=random.randint(1,6)
        val2=random.randint(1,6)
        print(f'({val1},{val2})')
        count+=1
        print('you have rolled the dice',count,'times')

    elif(choice=='n'):
        print('thanks for playing')
        break
    
    else:
        print('Invalid choice')
