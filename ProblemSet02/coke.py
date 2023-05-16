print("Amount due:50")
amount_due= 50
while amount_due>=0:
    coin= int(input("Insert coin: "))    
    if coin== 25 or coin== 10 or coin== 5:
        if amount_due-coin>0:    
            print("Amount due:", amount_due-coin)
            amount_due= amount_due- coin
        elif amount_due-coin<=0:
            amount_due= amount_due-coin
            print("Change owed:", amount_due*-1)
            break 
    else:
        print("Amount due:" ,amount_due)