import unittest

from solutions.day13.day13 import Track, create_track, Cart

SIMPLE_TRACK_FILE = 'examples/simple_track.txt'
LONGER_EXAMPLE_FILE = 'examples/longer_example.txt'


class TestDay13(unittest.TestCase):

    def test_simple_track(self):
        self.assertEqual(
            create_track(SIMPLE_TRACK_FILE),
            Track('/>\\\nv |\n\\-/')
        )

    # Moving one step puts a cart on a turn, which can't be read in for the underlying turn is hidden
    def test_move_two_steps(self):
        track = create_track(SIMPLE_TRACK_FILE)
        track.update(2)
        self.assertEqual(
            track,
            Track('/-\\\n| v\n\\>/')
        )

    def test_collision_on_last_moving_cart(self):
        track = create_track(SIMPLE_TRACK_FILE)
        track.update(3)
        expected = Track('/-\\\n| |\n\\-/')
        expected.carts = [Cart(2, 2, 'X'), Cart(2, 2, 'X')]
        self.assertEqual(
            track,
            expected
        )

    def test_collision_on_first_moving_cart(self):
        track = Track('/>\\\n\\>/')
        track.update(2)
        expected = Track('/-\\\n\\-/')
        expected.carts = [Cart(2, 1, 'X'), Cart(2, 1, 'X')]
        self.assertEqual(track, expected)

    def test_longer_example_till_first_turn(self):
        track = create_track(LONGER_EXAMPLE_FILE)
        track.update(1)
        expected = create_track(LONGER_EXAMPLE_FILE)
        expected.carts = [Cart(3, 0, '>'), Cart(9, 4, '>')]
        self.assertEqual(track, expected)

    def test_longer_example_till_second_turn(self):
        track = create_track(LONGER_EXAMPLE_FILE)
        track.update(4)
        expected = create_track(LONGER_EXAMPLE_FILE)
        expected.carts = [Cart(x=4, y=2, direction='>'), Cart(x=12, y=4, direction='^')]
        self.assertEqual(track, expected)

    def test_longer_example_till_third_turn(self):
        track = create_track(LONGER_EXAMPLE_FILE)
        track.update(7)
        expected = create_track(LONGER_EXAMPLE_FILE)
        expected.carts = [Cart(x=7, y=2, direction='>'), Cart(x=12, y=1, direction='<')]
        self.assertEqual(track, expected)

    def test_longer_example_till_fourth_turn(self):
        track = create_track(LONGER_EXAMPLE_FILE)
        track.update(11)
        expected = create_track(LONGER_EXAMPLE_FILE)
        expected.carts = [Cart(x=9, y=4, direction='<'), Cart(x=8, y=1, direction='<')]
        self.assertEqual(track, expected)
