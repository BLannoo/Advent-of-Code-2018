import unittest

from solutions.utils.utils import Location


class TestLocation(unittest.TestCase):
    def test_locations_can_be_sorted_in_reading_order(self):
        unsorted_locations = [
            Location(2, 2),
            Location(2, 1),
            Location(1, 2),
            Location(1, 1),
        ]
        unsorted_locations.sort()
        unsorted_locations.sort()
        self.assertEqual(
            unsorted_locations,
            [
                Location(1, 1),
                Location(1, 2),
                Location(2, 1),
                Location(2, 2),
            ]
        )
