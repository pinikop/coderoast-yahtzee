import unittest

from game.die import Die
from game.hand import Hand
from game.rules import (
    Aces,
    Chance,
    FibonYahtzee,
    FourOfAKind,
    FullHouse,
    LargeStraight,
    SmallStraight,
    ThreeOfAKind,
    Yahtzee,
)


class DieTestCase(unittest.TestCase):
    def test_sides_per_die(self):
        for _ in range(50):
            self.assertEqual(Die(sides=1).get_face(), 1)

    def test_set_face(self):
        die = Die(face=3)
        self.assertEqual(die.get_face(), 3)

    def test_to_string(self):
        die = Die()
        self.assertEqual(str(die.get_face()), str(die))

    def test_roll(self):
        for i in range(1, 20):
            die = Die(sides=i)
            for _ in range(10000):
                die.roll()
                self.assertTrue(1 <= die.get_face() <= i)


class HandTestCase(unittest.TestCase):
    def test_hand_number_of_dice(self):
        hand = Hand(15, 6)
        self.assertEqual(len(hand.hand), 15)

    def test_hand_sides_per_die(self):
        hand = Hand(5, 18)
        for i in hand.hand:
            self.assertEqual(i.sides, 18)


class RulesTestCase(unittest.TestCase):
    def test_aces(self):
        hand = Hand()
        hand.set_hand([1] * 5)
        self.assertEqual(Aces().score(hand), 5)

    def test_three_of_a_kind(self):
        hand = Hand()
        hand.set_hand([1, 1, 1, 2, 2])
        self.assertEqual(ThreeOfAKind().score(hand), 7)
        self.assertNotEqual(ThreeOfAKind().score(hand), 6)

    def test_four_of_a_kind(self):
        hand = Hand()
        hand.set_hand([1, 1, 1, 1, 2])
        self.assertEqual(FourOfAKind().score(hand), 6)

    def test_full_house(self):
        hand = Hand()
        hand.set_hand([2, 2, 3, 3, 3])
        self.assertEqual(FullHouse().score(hand), 25)

    def test_no_full_house(self):
        hand = Hand()
        hand.set_hand([2, 2, 4, 3, 3])
        self.assertEqual(FullHouse().score(hand), 0)

    def test_small_straight(self):
        hand = Hand()
        hand.set_hand([4, 3, 5, 2, 5])
        self.assertEqual(SmallStraight().score(hand), 30)
        hand.set_hand([4, 3, 3, 2, 5])
        self.assertEqual(SmallStraight().score(hand), 30)
        hand.set_hand([4, 1, 2, 2, 5])
        self.assertEqual(SmallStraight().score(hand), 0)

    def test_large_straight(self):
        hand = Hand()
        hand.set_hand([4, 3, 5, 2, 1])
        self.assertEqual(LargeStraight().score(hand), 40)
        hand.set_hand([4, 3, 5, 2, 6])
        self.assertEqual(LargeStraight().score(hand), 40)
        hand.set_hand([4, 1, 5, 2, 6])
        self.assertEqual(LargeStraight().score(hand), 0)

    def test_no_large_straight(self):
        hand = Hand()
        hand.set_hand([5, 3, 6, 2, 1])
        self.assertEqual(LargeStraight().score(hand), 0)

    def test_yahtzee(self):
        hand = Hand()
        hand.set_hand([3, 3, 3, 3, 3])
        self.assertEqual(Yahtzee().score(hand), 50)

    def test_chance(self):
        hand = Hand()
        hand.set_hand([1, 2, 3, 4, 5])
        self.assertEqual(Chance().score(hand), 15)

    def test_fibonyahtzee(self):
        hand = Hand()
        hand.set_hand([1, 1, 2, 3, 5])
        self.assertEqual(FibonYahtzee().score(hand), 100)
        hand.set_hand([2, 1, 2, 3, 5])
        self.assertEqual(FibonYahtzee().score(hand), 0)


if __name__ == "__main__":
    unittest.main()
