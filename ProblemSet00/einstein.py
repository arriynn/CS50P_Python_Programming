m = int(input("m: "))
c = pow (300_000_000,2)
E = (f"{m*c:,}")

print(E)

#_______________________________#

def main():
    m= int(input("m: "))
    energy(m)

def energy(e):
    c= pow(300_000_000, 2)
    print(f"{e*c: ,}", "Joules")

main()