import sys
if len(sys.argv)!=2:
    sys.exit("Invalid command-line argument")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python a file")



file_name= sys.argv[1]
count=0
try:
    with open(file_name, "r") as file:
        lines= file.readlines()

except FileNotFoundError:
    sys.exit("No such file in directory")

for line in lines:
    line= line.strip()
    if line and not line.startswith("#"):
        count+=1

print(count)
