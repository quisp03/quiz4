class Pokemon:
    def __init__(self, name, level):

        self._name = name
        self._level = level

    @property

    def level(self):
        return self._level

    @level.setter

    def level(self, value):

        if value < 1 or value > 100:
            raise ValueError("Level is capped between 1 and 100!")
        self._level = value