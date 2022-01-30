import random
a=random.randint(1,101)
userguess=None
guesses=0
while(userguess!=a):
    userguess=int(input("Enter your guess:"))
    guesses+=1
    if(userguess==a):
        print("You guessed it right!")
    else:
        if(userguess>a):
            print("You guessed it wrong! Enter a smaller number")
        else:
            print("You guessed it wrong! Enter a larger number")   
print(f"you guessed the number in {guesses} guesses")

