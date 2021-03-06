import unittest
from typing import List
import re


class ScoreBoard:
    def __init__(self, recipes: List[int], first_elf: int, second_elf: int):
        self.recipes = recipes
        self.first_elf = first_elf
        self.second_elf = second_elf

    def brew(self, iterations: int = 1):
        for _ in range(iterations):
            self.__brew()

    def __brew(self):
        recipe_first_elf = self.recipes[self.first_elf]
        recipe_second_elf = self.recipes[self.second_elf]
        recipe_sum = recipe_first_elf + recipe_second_elf
        if recipe_sum >= 10:
            self.recipes.append(recipe_sum // 10)
        self.recipes.append(recipe_sum % 10)
        number_of_recipes = len(self.recipes)
        self.first_elf = (self.first_elf + 1 + recipe_first_elf) % number_of_recipes
        self.second_elf = (self.second_elf + 1 + recipe_second_elf) % number_of_recipes

    def __find_new_recipe_index(self, current_index: int) -> int:
        return (current_index + 1 + self.recipes[current_index]) % len(self.recipes)

    def __eq__(self, other):
        return (
                isinstance(other, ScoreBoard)
                and
                self.recipes == other.recipes
                and
                self.first_elf == other.first_elf
                and
                self.second_elf == other.second_elf
        )

    def __repr__(self):
        return (
                "ScoreBoard(recipes=" + str(self.recipes)
                + ", first_elf=" + str(self.first_elf)
                + ", second_elf=" + str(self.second_elf)
                + ")"
        )

    def score(self, start):
        return "".join([
            str(recipe)
            for recipe in self.recipes[start:start + 10]
        ])

    def find(self, pattern: str):
        return re.search(pattern,
                         "".join([str(recipe) for recipe in self.recipes])
                         ).start()


class Day14TestCase(unittest.TestCase):
    def test_initial_scoreboard(self):
        self.assertEqual(
            [3, 7],
            ScoreBoard([3, 7], 0, 1).recipes
        )

    def test_brew_1(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(1)
        self.assertEqual(
            ScoreBoard([3, 7, 1, 0], 0, 1),
            score_board
        )

    def test_brew_2(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(2)
        self.assertEqual(
            ScoreBoard([3, 7, 1, 0, 1, 0], 4, 3),
            score_board
        )

    def test_brew_15(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(15)
        self.assertEqual(
            ScoreBoard(
                [3, 7, 1, 0, 1, 0, 1, 2, 4, 5, 1, 5, 8, 9, 1, 6, 7, 7, 9, 2],
                8, 4
            ),
            score_board
        )

    def test_score_after_5(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(15)
        self.assertEqual(
            "0124515891",
            score_board.score(5)
        )

    def test_score_after_9(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(10+9*2)
        self.assertEqual(
            "5158916779",
            score_board.score(9)
        )

    def test_score_after_18(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(10+18*2)
        self.assertEqual(
            "9251071085",
            score_board.score(18)
        )

    def test_score_after_2018(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(10+2018*2)
        self.assertEqual(
            "5941429882",
            score_board.score(2018)
        )

    def score_part_I(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(10+380621*2)
        self.assertEqual(
            "6985103122",
            score_board.score(380621)
        )

    def test_search_51589(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(20)
        self.assertEqual(
            9,
            score_board.find("51589")
        )

    def test_search_01245(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(20)
        self.assertEqual(
            5,
            score_board.find("01245")
        )

    def test_search_92510(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(20)
        self.assertEqual(
            18,
            score_board.find("92510")
        )

    def test_search_59414(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(2018)
        self.assertEqual(
            2018,
            score_board.find("59414")
        )

    # takes 36 sec
    def search_part_II(self):
        score_board = ScoreBoard([3, 7], 0, 1)
        score_board.brew(25000000)
        self.assertEqual(
            20182290,
            score_board.find("380621")
        )
