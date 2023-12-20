#!/usr/bin/env python

"""Yahtzee, the board game!

This python program will simulate a game of Yahtzee
"""

import os
import re
from typing import Optional

from game import Hand, ScoreBoard
from game.rules import *


class YahtzeeGame:
    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def __init__(self) -> None:
        self.clear_screen()
        print(
            """
        YAHTZEE

        Welcome to the game. To begin, simply press [Enter]
        and follow the instructions on the screen.

        To exit, press [Ctrl+C]
        """
        )

        # Begin by instantiating the hand and scoreboard
        self.hand = Hand()
        self.scoreboard = ScoreBoard()

        self.scoreboard.register_rules(
            [
                Aces(),
                Twos(),
                Threes(),
                Fours(),
                Fives(),
                Sixes(),
                ThreeOfAKind(),
                FourOfAKind(),
                FullHouse(),
                SmallStraight(),
                LargeStraight(),
                Yahtzee(),
                Chance(),
            ]
        )

    def show_scoreboard_points(self, hand: Optional[Hand] = None):
        print("\nSCOREBOARD")
        print("===================================")
        print(self.scoreboard.view_points(hand))
        print("===================================")

    def select_scoring(self):
        self.show_scoreboard_points(self.hand)
        while True:
            scoreboard_row = input("Choose which scoring to use: ")
            try:
                scoreboard_row_int = int(re.sub("[^0-9,]", "", scoreboard_row))
                if (
                    scoreboard_row_int < 1
                    or scoreboard_row_int > self.scoreboard.rules_count
                ):
                    print("Please select an existing scoring rule.")
                else:
                    return self.scoreboard.get_rule(scoreboard_row_int - 1)
            except ValueError:
                print("You entered something other than a number. Please try again")

    def choose_dice_reroll(self) -> list[int]:
        while True:
            try:
                reroll = input(
                    "\nChoose which dice to re-roll "
                    "(comma-separated or 'all'), or 0 to continue: "
                )

                if reroll.lower() == "all":
                    reroll = self.hand.all_dice()

                else:
                    # Perform some clean-up of input
                    reroll = reroll.replace(" ", "")  # Remove spaces
                    reroll = re.sub("[^0-9,]", "", reroll)  # Remove non-numerals
                    reroll = reroll.split(",")  # Turn string into list
                    reroll = list(map(int, reroll))  # Turn strings in list to int

                if not reroll or 0 in reroll:
                    return []
                else:
                    return reroll

            except ValueError:
                print("You entered something other than a number.")
                print("Please try again")

    def do_turn(self):
        rolls = 0
        selected_dice = self.hand.all_dice()
        while True:
            print(f"\nRolling Dice... {rolls}")
            self.hand.roll(selected_dice)
            print(self.hand)
            rolls += 1

            # if we reached maximum number of rolls, we are done
            if rolls >= 3:
                break

            # choose which dice to re-roll
            selected_dice = self.choose_dice_reroll()

            if len(selected_dice) == 0:
                break

            rule = self.select_scoring()
            points = self.scoreboard.assign_points(rule, self.hand)
            print(f"Adding {points} points to {rule.name}")
            self.show_scoreboard_points()

            input("\nPress any key to continue")
            self.clear_screen()

    def play(self):
        # We keep going until the scoreboard is full
        for _ in range(self.scoreboard.rules_count):
            self.do_turn()
        print("\nCongratulations! You finished the game!\n")
        self.show_scoreboard_points()
        print(f"Total points: {self.scoreboard.total_points}")


if __name__ == "__main__":
    try:
        game = YahtzeeGame()
        game.play()
    except KeyboardInterrupt:
        print("\nExiting...")
