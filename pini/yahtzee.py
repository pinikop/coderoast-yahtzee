#!/usr/bin/env python

"""Yahtzee, the board game!

This python program will simulate a game of Yahtzee
"""

import os
import re
from typing import Optional

from game import Hand, ScoreBoard
from game.rules import *

ROUNDS = {1: "1st", 2: "2nd", 3: "3rd"}


class YahtzeeGame:
    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def __init__(self) -> None:
        self.clear_screen()
        input(
            """
        YAHTZEE

        Welcome to the game. To begin, simply press [Enter]
        and follow the instructions on the screen.

        To exit, press [Ctrl+C]
        """
        )

        # Begin by instantiating the scoreboard
        rules_list = [
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

        self.scoreboard = ScoreBoard(rules_list)
        self.__n_dices = 5
        self.__all_dices = list(range(1, self.__n_dices + 1))

    def show_scoreboard_points(self, hand: Optional[Hand] = None):
        print("\nSCOREBOARD")
        print("===================================")
        print(self.scoreboard.view_points(hand))
        print("===================================")

    def select_scoring(self):
        while True:
            try:
                scoreboard_row = int(input("Choose which scoring to use: "))
                if not (1 <= scoreboard_row <= self.scoreboard.rules_count):
                    print("Please select an existing scoring rule.")
                elif scoreboard_row in self.scoreboard.rules_used:
                    print("Please select a new scoring rule")
                else:
                    return scoreboard_row
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
                    reroll = self.__all_dices

                else:
                    # Perform some clean-up of input
                    reroll = reroll.replace(" ", "").split(",")
                    reroll = list(map(int, reroll))  # Turn strings in list to int

                if not reroll or 0 in reroll:
                    return []
                elif not all(num in self.__all_dices for num in reroll):
                    print(
                        "You tried to reroll a die that doesn't exist. \nPlease try again"
                    )
                else:
                    return reroll

            except ValueError:
                print("You entered something other than a number.")
                print("Please try again")

    def play_round(self):
        hand = Hand(dice=self.__n_dices)
        selected_dice = hand.all_dice()
        rolls = 1
        while rolls <= 3:
            print(f"\nRolling Dice... {ROUNDS[rolls]} roll")
            if rolls > 1:
                # choose which dice to re-roll
                selected_dice = self.choose_dice_reroll()
                hand.roll(selected_dice)
            print(hand)
            self.show_scoreboard_points(hand)
            rolls += 1

            # if we reached maximum number of rolls, we are done
            if rolls > 3 or len(selected_dice) == 0:
                rule = self.select_scoring()
                points = self.scoreboard.assign_points(rule, hand)
                print(f"Adding {points} points to {self.scoreboard.rules[rule].name}")
                self.show_scoreboard_points()
                self.scoreboard.rules_used.add(rule)

                input("\nPress any key to continue")
                self.clear_screen()
                break

    def play_game(self):
        # We keep going until the scoreboard is full
        for _ in range(self.scoreboard.rules_count):
            self.play_round()
        print("\nCongratulations! You finished the game!\n")
        self.show_scoreboard_points()
        print(f"Total points: {self.scoreboard.total_points}")


if __name__ == "__main__":
    try:
        game = YahtzeeGame()
        game.play_game()
    except KeyboardInterrupt:
        print("\nExiting...")
