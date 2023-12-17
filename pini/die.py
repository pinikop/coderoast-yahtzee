import random
from typing import Optional


class Die:
    def __init__(self, sides=6, face: Optional[int] = None):
        self.sides = sides
        if face is not None:
            self.set_face(face)
        else:
            self.set_face(random.randint(1, self.sides))

    def set_face(self, value: int):
        self.__face = value

    def get_face(self):
        return self.__face

    def __str__(self):
        return str(self.__face)
