from typing import List, Optional

from game import Hand
from game.rules import Rule


class ScoreBoard:
    def __init__(self):
        self.rules: List[Rule] = []
        self.points: List[Optional[int]] = []

    @property
    def rules_count(self):
        return len(self.rules)

    def register_rules(self, rule: List):
        self.rules.extend(rule)
        self.points = [None] * self.rules_count

    def get_rule(self, row: int):
        return self.rules[row]

    def assign_points(self, rule: Rule, hand: Hand):
        row = self.rules.index(rule)
        if self.points[row] is not None:
            raise Exception("ScoreBoard already saved!")
        points = rule.assign_points(hand)
        self.points[row] = points
        return points

    @property
    def total_points(self):
        return sum(x for x in self.points if x is not None)

    def view_points(self, hand: Optional[Hand] = None):
        strs = []
        padding = max(len(rule.name) for rule in self.rules)
        for idx, rule in enumerate(self.rules):
            points = self.points[idx]
            view_str = f"{idx + 1:>2}. {rule.name:.<{padding + 1}}: "
            if hand is not None and points is None:
                view_str += f"+ {rule.assign_points(hand):>2} points ***"
            elif points is not None:
                view_str += f"{points:>4} points"
            strs.append(view_str)
        return "\n".join(strs)
