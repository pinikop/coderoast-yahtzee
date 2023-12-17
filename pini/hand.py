from die import Die


class Hand:
    def __init__(self, n_dice=5, n_sides=6):
        self.n_dice = n_dice
        self.n_sides = n_sides
        self.hand = [Die(self.n_sides) for _ in range(self.n_dice)]

    def roll(self, dice):
        if not all(1 <= num <= self.n_dice for num in dice):
            raise IndexError("Dice must be between 1 and " + str(self.n_dice))
        for die in dice:
            self.hand[die - 1] = Die(self.n_sides)

    def get_hand(self):
        return [die.get_face() for die in self.hand]

    def set_hand(self, values):
        self.hand = [Die(self.n_sides, val) for val in values]

    def count_occurrences(self, face):
        return self.get_hand().count(face)

    def sum_hand(self):
        return sum(self.get_hand())

    def __str__(self) -> str:
        return "\n".join(
            [f"die {die+1} has value {face}" for die, face in enumerate(self.hand)]
        )
