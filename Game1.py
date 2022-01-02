import random
#Snake water gun or Rock Paper Scissors game
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("comp turn: I have chose, now it's your turn")
randno=random.randint(1,3)
if randno==1:
    comp='s'
elif randno==2:
    comp='w'
elif randno==3:
    comp='g'

you=input("Your turn: Snake(s) water(w) or gun(g)?")
a=gamewin(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")

if a==None:
    print("the game is a tie!")
elif a:
    print("You win!")
else:
    print("You lose!")