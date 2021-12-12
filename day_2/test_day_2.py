import unittest

from day_2 import Day2

class TestDay2(unittest.TestCase):

    def test_part_1(self):
        result = Day2.part_1(self, 'test_input_2.txt')
        self.assertEqual(result, 150)

    def test_part_2(self):
        result = Day2.part_2(self, 'test_input_2.txt')
        self.assertEqual(result, 900)

if __name__ == '__main__':
    unittest.main()
