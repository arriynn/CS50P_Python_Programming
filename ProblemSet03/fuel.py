def main():
    
    fuel= input("Fracton: ")
    print(gauge(convert(fuel)))
    


def convert(fraction):
    while True:
        try: 
            n, d= fraction.split("/")
            n= int(n)
            d= int(d)
            return n/d*100

        except (ValueError, ZeroDivisionError, TypeError):
            print("", end="")

def gauge(percentage):
    if percentage== 100:
        return "F"
    elif percentage== 0:
        return "E"
    else:
        return (f"{percentage: .0f}%")

if __name__=="__main__":
    main()