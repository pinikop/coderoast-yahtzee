from collections import Counter

from .die import Die


class Hand:
    def __init__(self, dice: int = 5, sides: int = 6):
        """_summary_

        Args:
            dice (int, optional): The number of dice in the hand. Defaults to 5.
            sides (int, optional): the Number of sides each die has. Defaults to 6.
        """
        self.dice = dice
        self.sides = sides
        self.hand = [Die(self.sides) for _ in range(self.dice)]

    def roll(self, dice: list[int]) -> None:
        """rolls the specified dice

        Args:
            dice (list[int]): dice to roll

        Raises:
            IndexError: if a die that is not in the hand
        """
        if not all(1 <= num <= self.dice for num in dice):
            raise IndexError("Dice must be between 1 and " + str(self.dice))
        for i in dice:
            self.hand[i - 1].roll()

    def get_hand(self) -> list[int]:
        """Returns the hand as a list of integers"""
        return [die.get_face() for die in self.hand]

    def set_hand(self, values):
        """Sets the hand to the specified values"""
        self.hand = [Die(self.sides, val) for val in values]

    @property
    def counter(self) -> Counter:
        """Returns a Counter of the values in the hand"""
        return Counter(self.get_hand())

    def count_occurrences(self, face) -> int:
        """Returns the number of occurrences of the specified face in the hand"""
        return self.counter[face]

    @property
    def sum(self) -> int:
        """Returns the sum of the values in the hand"""
        return sum(self.get_hand())

    def __str__(self) -> str:
        return "\n".join(
            [f"die {die+1} has value {face}" for die, face in enumerate(self.hand)]
        )
