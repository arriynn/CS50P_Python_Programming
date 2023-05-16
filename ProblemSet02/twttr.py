def main():

    tweet= input("Input: ")
    print(shorten(tweet))
def shorten(word):
    vowel= ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for t in word:
        if t in vowel:
            word= word.replace(t, "")
    return word
if __name__=="__main__":
    main()