from dataclasses import dataclass
from typing import Dict, List, Optional, Set

from game import Hand
from game.rules import Rule


@dataclass
class GameRule:
    """Class to store Rule information"""

    rule: Rule
    points: Optional[int] = None

    @property
    def name(self) -> str:
        """print the name of the rule"""
        return self.rule.name


class ScoreBoard:
    def __init__(self, rules):
        self.rules: Dict[int, GameRule] = self.__register_rules(rules)
        self.rules_used: Set[int] = set()

    @property
    def rules_count(self) -> int:
        """Count total number of rules in the scoreboard"""
        return len(self.rules)

    @classmethod
    def __register_rules(cls, rules_list: List[Rule]) -> Dict[int, GameRule]:
        return {i: GameRule(rule=rule) for i, rule in enumerate(rules_list, start=1)}

    def get_rule(self, row: int) -> Rule:
        return self.rules[row].rule

    def assign_points(self, row: int, hand: Hand) -> int:
        if self.rules[row].points is not None:
            raise Exception("ScoreBoard already saved!")
        points = self.rules[row].rule.assign_points(hand)
        self.rules[row].points = points
        return points

    @property
    def total_points(self) -> int:
        return sum(
            rule.points for rule in self.rules.values() if rule.points is not None
        )

    def view_points(self, hand: Optional[Hand] = None) -> str:
        strs = []
        padding = max(len(rule.name) for rule in self.rules.values())
        for idx, rule in self.rules.items():
            points = self.rules[idx].points
            view_str = f"{idx:>2}. {rule.name:.<{padding + 1}}: "
            if hand is not None and points is None:
                view_str += f"+ {rule.rule.assign_points(hand):>2} points ***"
            elif points is not None:
                view_str += f"{points:>4} points"
            strs.append(view_str)
        return "\n".join(strs)
