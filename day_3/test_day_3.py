import unittest

from day_3 import Day3

class TestDay3(unittest.TestCase):

    def test_part_1(self):
        result = Day3.part_1(self, 'test_input_3.txt')
        self.assertEqual(result, 198)

    def test_part_2(self):
        result = Day3.part_2(self, 'test_input_3.txt')
        self.assertEqual(result, 230)

if __name__ == '__main__':
    unittest.main()
