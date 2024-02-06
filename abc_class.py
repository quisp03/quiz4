from abc import ABC, abstractmethod

class Pokemon(ABC):

    @abstractmethod

    def fight(self):
        pass

    @abstractmethod

    def run(self):
        pass


class Mewtwo(Pokemon):
    def fight(self):
        return "Mewtwo uses Psystrike!!"
    
    def run(self):
        return "Mewtwo got away safely!!"
    

class Geodude(Pokemon):
    def fight(self):
        return "Geodude uses Earthquake!!"
    
    def run(self):
        return "Geodude got away safely!!"