class Students:
    def __init__(self, name, house):
        self.name= name
        self.house= house
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name= input("Name: ").strip()
        house= input("House: ").strip()
        return cls(name, house)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name (self, name):
        if not name:
            raise ValueError("Missing name")
        self._name= name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ["Griffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]:
            raise ValueError("Invalid house")
        self._house= house 

def main():
    print(Students.get())
    

    

if __name__=="__main__":
    main()