import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count=0
    words= s.split(" ")
    for word in words:
        if word=="umm" or word=="UMM":
            count+=1

    return count





if __name__ == "__main__":
    main()