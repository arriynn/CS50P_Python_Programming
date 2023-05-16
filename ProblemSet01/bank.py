def main():
    greet= input("Greeting: ").lower().strip()
    print(value(greet))
def value(greeting):
    if "hello" in greeting:
        return "$0"
    elif greeting.startswith("h")== True:
        return "$20"
    else:
        return "$100"
    
if __name__=="__main__":
    main()