import inflect
p= inflect.engine()

names=["Adieu", "adieu"]

while True:
    try:
        name= input("Name: ")
        names.append(name)
    except KeyboardInterrupt:
        print()
        break
names[2]= "to "+names[2]

if len(names)==3:
    names= p.join(names, conj="")
elif len(names)==4:
    names= p.join(names, final_sep="")
else:
    names= p.join(names)
print(names)