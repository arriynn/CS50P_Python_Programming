def main():
    yell("this", "is", "CS50")


def yell(*phrase):
    uppercased= [word.upper() for word in phrase]

    print(*uppercased)

if __name__=="__main__":
    main()