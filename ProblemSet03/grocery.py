glist= {}
while True:
    try:
        item= input("Item: ").lower()
        if item in glist:
            glist[item]= glist[item]+ 1
        else:
            glist[item]=1
    except KeyboardInterrupt:
        print("\n")
        for key in sorted(glist.keys()):
            print(glist[key], key.upper())
        break