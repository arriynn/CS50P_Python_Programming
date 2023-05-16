def main():
    sentence= input()
    convert(sentence)

def convert(emoticon):
    print(emoticon.replace(":(", "🙁").replace(":)", "🙂"))

main()
