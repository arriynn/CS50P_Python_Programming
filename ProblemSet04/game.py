import random
while True:
    try:
        level= int(input("Level: "))
        if level>0:
            break
    except ValueError:
        print("", end="")
while True:
    try:
        guess= int(input("Guess: "))
        if guess>0:
            break
    except ValueError:
        print("", end="")
number= random.randint(1,level)
if guess>number:
    print("Too Large")
elif guess<number:
    print("Too Small")
else:
    print("Just Right")