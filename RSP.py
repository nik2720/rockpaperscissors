'''
Created on Jan 12, 2019

@author: Nik


'''




import random 
moves=['r','s','p']
a=0



def endscreen():
    userend=input("enter y to play again. enter n to quit")
    if userend == 'y':
        game()
    if userend == 'n':
        exit()
    if userend != 'y' or 'n':
        print("that was an invalid command")
        endscreen()



print("welcome to rock scissors and paper")

def game():

    while a != 2:
        computer=random.choice(moves)
       
        user=str(input("enter r for rock, s for scissors, and p for paper: "))







        if user == computer:
            print("user picked " ,user, "computer picked " ,computer)
            print("its a draw ")
            endscreen()

        if user =='r' and computer == 'p':
            print("user picked " ,user, "computer picked " ,computer)
    
            print("computer wins ")
            endscreen()
        if user =='r' and computer == 's':
            print("user picked " ,user, "computer picked " ,computer)
            print("user wins")
            endscreen()
        if user =='s' and computer == 'p':
            print("user picked " ,user, "computer picked " ,computer)
            print("user wins")
        if user =='s' and computer == 'r':    
    
            print("user picked " ,user, "computer picked " ,computer)
            print("computer wins")
            endscreen()
        if user =='p' and computer =='r':
            print("user picked " ,user, "computer picked " ,computer)
            print("user wins")
            endscreen()
        if user =='p' and computer =='s':
            print("user picked " ,user, "computer picked " ,computer)
            print("computer wins") 
            endscreen()
        if user not in moves:
            print("that was an invalid command")
            
            
game()
