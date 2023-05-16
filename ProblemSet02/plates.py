def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<4:
        return False
    if s[0:2].isalpha()== False:
        return False
    for i in range(len(s)-1):
        if s[i].isnumeric()== True:
            if s[i]== "0":
                return False
            elif (i<len(s)-1 and s[i+1].isalpha()== True):
                return False                
    for c in s:
        if c in [",", " ", ".", "!"]:
            return False
    else:
        return True
if __name__=="__main__":
    main()