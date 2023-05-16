students= [
           {"name": "Harry", "house": "Gryffindor", "patronous": "Stag"},
{"name":"Herminone", "house": "Gryffindor", "patronous":"Otter"},
{"name": "Draco", "house":"Slytherin", "patronous": None}
]
 
for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", ")
