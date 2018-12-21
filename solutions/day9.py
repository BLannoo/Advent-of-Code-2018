import unittest

MULTIPLE = 23


class Marble:
    def __init__(self, points, clock_wise=None, counter_clock_wise=None):
        self.__points = points
        self.__clock_wise = clock_wise
        if clock_wise == None:
            self.__clock_wise = self
        self.__counter_clock_wise = counter_clock_wise
        if counter_clock_wise == None:
            self.__counter_clock_wise = self

    def __insert_between(self, counter_clock_wise, clock_wise):
        self.__clock_wise = clock_wise
        self.__counter_clock_wise = counter_clock_wise
        clock_wise.__counter_clock_wise = self
        counter_clock_wise.__clock_wise = self

    def __remove_marble(self):
        old_counter_clock_wise = self.__counter_clock_wise
        old_clock_wise = self.__clock_wise
        old_clock_wise.__counter_clock_wise = old_counter_clock_wise
        old_counter_clock_wise.__clock_wise = old_clock_wise

    def get_counter_clockwise(self, times: int) -> 'Marble':
        if times == 0:
            return self
        return self.__counter_clock_wise.get_counter_clockwise(times - 1)

    def play_marble(self, new_marble: 'Marble') -> ('Marble', int):
        if not new_marble.__points % MULTIPLE == 0:
            clock_wise_1 = self.__clock_wise
            clock_wise_2 = clock_wise_1.__clock_wise
            new_marble.__insert_between(clock_wise_1, clock_wise_2)
            return new_marble, 0
        else:
            to_be_removed = self.get_counter_clockwise(7)
            next_focus = to_be_removed.__clock_wise
            to_be_removed.__remove_marble()
            return next_focus, new_marble.__points + to_be_removed.__points

    def __circle_str_till(self, s, last_marble):
        if self.__points < 10:
            s += ' '
        s += str(self.__points) + ' '
        if self == last_marble:
            return s
        return self.__clock_wise.__circle_str_till(s, last_marble)

    def circle_str(self):
        return self.__circle_str_till('', self.__counter_clock_wise)

    def __repr__(self):
        return (
                'Marble(points='
                + str(self.__points)
                + ', clock_wise_points='
                + str(self.__clock_wise.__points)
                + ', counter_clock_wise_points='
                + str(self.__counter_clock_wise.__points)
                + ')'
        )


def play(step):
    m0 = Marble(0)
    current_marble = m0
    for i in range(1, step + 1):
        new_marble = Marble(i)
        current_marble = current_marble.play_marble(new_marble)
    return m0


class Game:
    def __init__(self, number_of_players):
        self.__players = [0 for _ in range(number_of_players)]
        self.__first_marble = Marble(0)
        self.__current_marble = self.__first_marble

    def play(self, turns: int):
        for i in range(1, turns + 1):
            self.__current_marble, points_earned = self.__current_marble.play_marble(Marble(i))
            self.__players[i % len(self.__players)] += points_earned

    def __repr__(self):
        return self.__first_marble.circle_str()

    def high_score(self) -> int:
        return max(self.__players)


class TestDay9(unittest.TestCase):
    def test_step_22(self):
        game = Game(1)
        game.play(22)
        self.assertEqual(
            ' 0 16  8 17  4 18  9 19  2 20 10 21  5 22 11  1 12  6 13  3 14  7 15 ',
            str(game)
        )

    def test_step_23(self):
        game = Game(1)
        game.play(23)
        self.assertEqual(
            ' 0 16  8 17  4 18 19  2 20 10 21  5 22 11  1 12  6 13  3 14  7 15 ',
            str(game)
        )

    def test_step_24(self):
        game = Game(1)
        game.play(24)
        self.assertEqual(
            ' 0 16  8 17  4 18 19  2 24 20 10 21  5 22 11  1 12  6 13  3 14  7 15 ',
            str(game)
        )

    def test_1_player_step_23(self):
        game = Game(1)
        game.play(23)
        self.assertEqual(
            32,
            game.high_score()
        )

    def test_10_player_step_1618(self):
        game = Game(10)
        game.play(1618)
        self.assertEqual(
            8317,
            game.high_score()
        )

    def test_part_1(self):
        game = Game(435)
        game.play(71184)
        self.assertEqual(
            412959,
            game.high_score()
        )

    def test_part_2(self):
        game = Game(435)
        game.play(7118400)
        self.assertEqual(
            3333662986,
            game.high_score()
        )
