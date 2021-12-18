import unittest

from day_6 import Day6

class TestDay6(unittest.TestCase):

    def test_part_1(self):
        result = Day6.part_1(self, 'test_input_6.txt', 18)
        self.assertEqual(result, 26)

        result2 = Day6.part_1(self, 'test_input_6.txt', 80)
        self.assertEqual(result2, 5934)

    def test_part_2(self):
        result = Day6.part_2(self, 'test_input_6.txt', 18)
        self.assertEqual(result, 26)

        result2 = Day6.part_2(self, 'test_input_6.txt', 80)
        self.assertEqual(result2, 5934)

if __name__ == '__main__':
    unittest.main()
