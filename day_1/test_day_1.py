import unittest

from day_1 import Day1

class TestDay1(unittest.TestCase):

    def test_part_1(self):
        result = Day1.part_1(self, 'test_input_1_1.txt')
        self.assertEqual(result, 7)

    def test_part_2(self):
        result = Day1.part_2(self, 'test_input_1_2.txt')
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
