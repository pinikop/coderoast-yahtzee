import random
from typing import Optional


class Die:
    def __init__(self, sides=6, face: Optional[int] = None):
        self.sides = sides
        self.roll() if face is None else self.set_face(face)

    def roll(self) -> None:
        """Rolls the Die"""
        self.__face = random.randint(1, self.sides)

    def set_face(self, value: int) -> None:
        """Sets the face of the Die"""
        if value not in range(1, self.sides + 1):
            raise ValueError(f"Face value must be between 1 and {self.sides}")
        self.__face = value

    def get_face(self) -> int:
        """Returns the face of the Die"""
        return self.__face

    def __str__(self):
        return str(self.__face)
