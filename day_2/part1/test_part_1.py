import unittest
from day_2.part1.puzzle_part_1 import Puzzle


class TestPart1(unittest.TestCase):

    def test_1(self):
        p = Puzzle()
        p.parse_file_input(file='test_part1')
        result = p.run()
        self.assertEqual(12, result)

    def test_answer_1(self):
        p = Puzzle()
        p.parse_file_input(file='input_part_1')
        result = p.run()
        print("Answer is {}".format(result))
        self.assertIsInstance(result, int)
