from dataclasses import dataclass

@dataclass

class Pokemon:
    name: str
    type: str
    level: int

    def level_up(self):
        self.level = self.level +1
        return f"{self.name} of {self.type} type has leveled up to {self.level}!"