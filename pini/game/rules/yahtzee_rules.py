from dataclasses import dataclass

from ..hand import Hand
from .base_rules import FixPointsRule, NOfAKind, Rule, SameValueRule, Straight


@dataclass
class Aces(SameValueRule):
    rule_name: str = "Aces"
    value: int = 1


@dataclass
class Twos(SameValueRule):
    rule_name: str = "Twos"
    value: int = 2


@dataclass
class Threes(SameValueRule):
    rule_name: str = "Threes"
    value: int = 3


@dataclass
class Fours(SameValueRule):
    rule_name: str = "Fours"
    value: int = 4


@dataclass
class Fives(SameValueRule):
    rule_name: str = "Fives"
    value: int = 5


@dataclass
class Sixes(SameValueRule):
    rule_name: str = "Sixes"
    value: int = 6


@dataclass
class ThreeOfAKind(NOfAKind):
    rule_name: str = "Three of a kind"
    value: int = 3


@dataclass
class FourOfAKind(NOfAKind):
    rule_name: str = "Four of a kind"
    value: int = 4


@dataclass
class FullHouse(FixPointsRule):
    rule_name: str = "Full house"
    _points: int = 25

    def to_score(self, hand: Hand) -> bool:
        return set([2, 3]) == set(hand.counter.values())


@dataclass
class SmallStraight(Straight):
    rule_name: str = "Small straight"
    size: int = 4
    _points: int = 30


@dataclass
class LargeStraight(Straight):
    rule_name: str = "Large straight"
    size: int = 5
    _points: int = 40


@dataclass
class Yahtzee(FixPointsRule):
    rule_name: str = "Yahtzee"
    _points: int = 50

    def to_score(self, hand: Hand) -> bool:
        return len(set(hand.get_hand())) == 1


@dataclass
class FibonYahtzee(FixPointsRule):
    rule_name: str = "FibonYahtzee"
    _points: int = 100

    def to_score(self, hand: Hand) -> bool:
        return sorted(hand.get_hand()) == [1, 1, 2, 3, 5]


@dataclass
class Chance(Rule):
    rule_name: str = "Chance"

    def points(self, hand: Hand) -> int:
        return hand.sum

    def to_score(self, hand: Hand) -> bool:
        return True
