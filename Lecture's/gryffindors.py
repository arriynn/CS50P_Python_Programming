students= [
           {"name": "Harry", "house": "Gryffindor", "patronous": "Stag"},
{"name":"Herminone", "house": "Gryffindor", "patronous":"Otter"},
{"name": "Draco", "house":"Slytherin", "patronous": None}
]


gryffindors= filter(lambda s: s["house"]== "Gryffindor", students)

for gryffindor in sorted(gryffindors, key= lambda s: s["name"]):
    print(gryffindor["name"])