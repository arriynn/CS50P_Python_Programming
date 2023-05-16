import random
def main():
    lev= get_level()
    life=2
    score= 0
    for i in range(10):
        try:
            x= generate_integer(lev)
            y= generate_integer(lev)        
            problem= f"{x}+{y}="
            answer= x + y
            user_answer= int(input(problem))
            for j in range(2):
                if user_answer==answer:
                    score+=1
                    break
                elif user_answer!=answer:
                    life-=1
                    print("EEE")
                    user_answer= int(input(problem))
                    if life==0:
                        print(f"Answer: {answer}")
                        break
        except ValueError:
            continue
    print(f"Score: {score}/10")


def get_level():
    while True:
        try:
            level=input("Level :")
            if level in ["1", "2", "3"]:
                return int(level)
        except ValueError:
            print("EEE")

def generate_integer(level):
    if level==1:
        return random.randint(1,9)
    elif level==2:
        return random.randint(10, 99)
    elif level==3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__=="__main__":
    main()