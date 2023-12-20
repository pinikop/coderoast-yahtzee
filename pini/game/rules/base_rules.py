from dataclasses import dataclass
from typing import Optional

from ..hand import Hand


@dataclass
class Rule:
    rule_name: str

    @property
    def name(self):
        return self.rule_name

    def points(self, hand: Hand) -> int:
        ...

    def to_assign(self, hand: Optional[Hand] = None) -> bool:
        ...

    def assign_points(self, hand: Hand) -> int:
        return self.points(hand) if self.to_assign(hand) else 0


@dataclass
class SameValueRule(Rule):
    value: int

    def points(self, hand: Hand) -> int:
        return hand.count_occurrences(self.value) * self.value

    def to_assign(self, hand) -> bool:
        return True


@dataclass
class NOfAKind(Rule):
    value: int

    def points(self, hand: Hand) -> int:
        return hand.sum

    def to_assign(self, hand: Hand) -> bool:
        return max(hand.counter.values()) >= self.value


@dataclass
class FixPointsRule(Rule):
    _points: int

    def points(self, hand: Hand) -> int:
        return self._points


@dataclass
class Straight(FixPointsRule):
    size: int

    def to_assign(self, hand: Hand) -> bool:
        dice = set(hand.get_hand())
        return (len(dice) == self.size) and (max(dice) - min(dice) == (self.size - 1))
