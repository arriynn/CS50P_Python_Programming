class Vault:
    def __init__(self, sickles, galleons, knuts) -> None:
        self.sickles= sickles
        self.galleons= galleons
        self.knuts= knuts

    def __str__(self) -> str:
        return f"{self.galleons} Galleons, {self.sickles} Sickels, {self.knuts} Knuts"
    
    def __add__(self, other):
        galleons= self.galleons + other.galleons
        sickels= self.sickles + other.sickles 
        knuts= self.knuts + other.knuts
        return Vault(galleons, sickels, knuts)
    
    
potter= Vault(100,50, 25)
print(potter)

wesley= Vault(25,50, 100)
print(wesley)

total = potter+ wesley
print(total)