import sys
import csv
if len(sys.argv) <3:
    sys.exit("Too few arguments")
elif len(sys.argv)>3:
    sys.exit("Too many arguments")
elif not sys.argv[1].endswith(".csv") and not sys.argv[2].endswith(".csv"):
    sys.exit("Not a csv file")
 
with open(sys.argv[1], newline="") as file:
    reader= csv.DictReader(file)
    with open(sys.argv[2], "w") as file2:
        writer= csv.DictWriter(file2, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            row["first"]= row.pop("name")
            lastname, firstname= row["first"].split(",")
            row["last"]= lastname
            row["first"]= firstname
            writer.writerow(row)

