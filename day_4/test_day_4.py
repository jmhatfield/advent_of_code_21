import unittest

from day_4 import Day4

class TestDay4(unittest.TestCase):

    def test_part_1(self):
        result = Day4.part_1(self, 'test_input_4.txt')
        self.assertEqual(result, 4512)

    def test_part_2(self):
        result = Day4.part_2(self, 'test_input_4.txt')
        self.assertEqual(result, 1924)

if __name__ == '__main__':
    unittest.main()
