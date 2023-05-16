months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July", 
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date= input("Date: ").title().replace(",", "")
    try:
        month, day, year= date.split("/")
        if int(day)>=1 and int(day)<=31 and int(month)>=1 and int(month)<=12:
            print(f"{int(year)}-{int(month): 02}-{int(day)}")
            break
    except:
        month, day, year= date.split(" ")
        if int(day)>=1 and int(day)<=31:
            if month in months:
                    print(f"{int(year)}-{months.index(month)+1}- {day:0}")
                    break
