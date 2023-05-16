def main():
    time= input("Time: ")
    tme= convert(time)

    if 7<tme<8:
        print("Breakfast time")
    elif 12<tme<13:
        print("Lunch time")
    elif 18<tme<19:
        print("Dinner time")
    else:
        print()

def convert(t):
    hour, minute= t.split(":")
    t= float(hour) + float(minute)/60
    return t

if __name__ == "__main__":
    main()