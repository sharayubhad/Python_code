#Snake water gun game or stone paper scissor game!
import random
print("************WELCOME TO SNAKE WATER GUN GAME*************")

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp == 'w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True
        
while(1):
    print("Comp turn: Snake(s), Water(w) or gun(g)?")

    randNo = random.randint(1,3)
    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'w'
    elif randNo == 3:
        comp = 'g'

    you = input("Your turn: Snake(s), Water(w) or gun(g)?")

    print("Computer chose:"+comp)
    print("You chose:"+you)

    a = gameWin(comp,you)
    if a==None:
        print("The game is tie!")
    elif a==True:
        print("You win!")
    elif a==False:
        print("You lose!")

    a = input("Do you want to play again?(y/n):  ").lower()
    if(a!='y'):
        break
