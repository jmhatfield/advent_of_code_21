import unittest

from day_5 import Day5

class TestDay5(unittest.TestCase):

    def test_part_1(self):
        result = Day5.part_1(self, 'test_input_5.txt')
        self.assertEqual(result, 5)

    def test_part_2(self):
        result = Day5.part_2(self, 'test_input_5.txt')
        self.assertEqual(result, 12)
        pass

if __name__ == '__main__':
    unittest.main()
