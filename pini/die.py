import random
from typing import Optional


class Die:
    def __init__(self, face: Optional[int] = None, sides=6):
        self.sides = sides
        if face is not None:
            self.__face = face
        else:
            self.roll()

    def set_face(self, value: int):
        self.__face = value

    def get_face(self):
        return self.__face

    def roll(self):
        self.set_face(random.randint(1, self.sides))

    def __str__(self):
        return str(self.__face)
