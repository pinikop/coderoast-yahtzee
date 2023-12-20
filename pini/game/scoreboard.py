from typing import List, Optional

from game import Hand
from game.rules import Rule


class ScoreBoard:
    def __init__(self):
        self.rules = []
        self.points = []

    @property
    def rules_count(self):
        return len(self.rules)

    def register_rules(self, rule: List):
        self.rules.extend(rule)
        self.points = [0] * self.rules_count

    def get_rule(self, row: int):
        return self.rules[row]

    def assign_points(self, rule: Rule, hand: Hand):
        row = self.rules.index(rule)
        if self.points[row] > 0:
            raise Exception("ScoreBoard already saved!")
        points = rule.assign_points(hand)
        self.points[row] = points
        return points

    @property
    def total_points(self):
        return sum(self.points)

    def view_points(self, hand: Optional[Hand] = None):
        strs = []
        for idx, rule in enumerate(self.rules):
            points = self.points[idx]
            view_str = f"{idx + 1}. {rule.name}: "
            if hand is not None and points == 0 and rule.points > 0:
                view_str += f"+{rule.assign_points(hand)} points ***"
            else:
                view_str += f"{points} points"
            strs.append(view_str)
