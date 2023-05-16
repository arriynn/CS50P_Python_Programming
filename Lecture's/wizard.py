class Wizard:
    def __init__(self, name) -> None:
        if not name:
            raise ValueError
        self.name= name

class Students(Wizard):
    def __init__(self, name, house) -> None:
        super().__init__(name)

        self.house= house

class Professors(Wizard):
    def __init__(self, name, subject) -> None:
        super().__init__(name)
        self.subject = subject

student= Students("Harry", "Gryffindor")
professor= Professors("Albet", "Defence against the dark arts")
wizard= Wizard("Nigga")