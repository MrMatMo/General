import random

User_name = input('What\'s your name ?  ' )
User = 0
Bot = 0
Setnum = int (input('How many times you wanna play? '))
#for Set in range(0,Setnum):
while User < Setnum and Bot < Setnum:
    print(f'{User_name} = {User}  ,  PC = {Bot}')

    User_Choice = input (f'{User_name}, Rock , Paper or Scissors ??  ') .lower()
    PC_Choice = random.randint(0 , 1)
    if PC_Choice == 0 :
        PC_Choice = 'rock'
    elif PC_Choice == 1 :
        PC_Choice = 'paper'
    else:
        PC_Choice = 'scissors'

    print(f'{User_Choice} Vs. {PC_Choice}')

    if User_Choice == PC_Choice :
        print (" That's a Tie !! ")

    elif User_Choice == 'rock' :
        if PC_Choice == 'paper':
            print ('PC Wins !!')
            Bot += 1
        elif PC_Choice == 'scisoors' : 
            print (f'{User_name} Wins !!')
            User +=1

    elif User_Choice == 'paper' :
        if PC_Choice == 'rock':
            print (f'{User_name} You Win!!')
            User +=1
        elif PC_Choice == 'scisoors' : 
            print ('PC Wins !!')
            Bot += 1

    elif User_Choice == 'scissors' :
        if PC_Choice == 'paper':
            print (f'{User_name} You Win!!')
            User +=1
        elif PC_Choice == 'rock' : 
            print ('PC Wins !!')
            Bot += 1

    else:
        print("wrong input Babe")

print('--- GAME OVER ---')
print (f'{User_name} = {User}')
print (f'PC = {Bot}')
if Bot < User :
    print(f'{User_name},You Won !!')
else : 
    print('PC Won !!')
