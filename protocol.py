from typing import Protocol

class Pokemon(Protocol):
    def fight(self) ->str:
        pass

    def run(self) ->str:
        pass

class Mewtwo:
    def fight(self):
        return "Mewtwo uses Psystrike!!"
    
    def run(self):
        return "Mewtwo got away safely!!"
    

class Geodude:
    def fight(self):
        return "Geodude uses Earthquake!!"
    
    def run(self):
        return "Geodude got away safely!!"