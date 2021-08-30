import unittest

from utils import get_coordinates


class TestUtils(unittest.TestCase):
    def test_get_coordinates(self):
        location = 'Heart of the City Farmers Market at UN Plaza'

        want = 37.7798199, -122.4146615

        got = get_coordinates(location=location)

        self.assertEqual(want, got)

    def test_get_coordinates_fail(self):
        location = '200 block Market Street'

        want = 0, 0

        got = get_coordinates(location=location)

        self.assertEqual(want, got)


if __name__ == '__main__':
    unittest.main()
