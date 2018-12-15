import unittest

from solutions.day13.day13 import Track, create_track, Cart

SIMPLE_TRACK_FILE = 'examples/simple_track.txt'


class TestDay13(unittest.TestCase):

    def test_simple_track(self):
        self.assertEqual(
            create_track(SIMPLE_TRACK_FILE),
            Track('/>\\\nV |\n\\-/')
        )

    # Moving one step puts a cart on a turn, which can't be read in for the underlying turn is hidden
    def test_move_two_steps(self):
        track = create_track(SIMPLE_TRACK_FILE)
        track.update(2)
        self.assertEqual(
            track,
            Track('/-\\\n| V\n\\>/')
        )

    def test_collision(self):
        track = create_track(SIMPLE_TRACK_FILE)
        track.update(3)
        expected = Track('/-\\\n| |\n\\-/')
        expected.carts = [Cart(2, 2, 'X'), Cart(2, 2, 'X')]
        self.assertEqual(
            track,
            expected
        )
