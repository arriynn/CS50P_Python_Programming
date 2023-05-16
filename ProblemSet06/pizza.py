import sys
from tabulate import  tabulate

if len(sys.argv)<2:
    sys.exit("Too few arguments")
elif len(sys.argv)>2:
    sys.exit("Too many arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a csv file")

menu= sys.argv[1]

try:
    with open (menu, "r") as file:
        lines= file.readlines()

    data= [line.strip().split(",") for line in lines]
except FileNotFoundError:
    sys.exit("File not in directory")
        
table= tabulate(data, headers="firstrow", tablefmt="grid")    

print(table)
