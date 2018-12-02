import unittest
from day_2.part2.puzzle_part_2 import Puzzle


class TestPart2(unittest.TestCase):

    def test_2(self):
        p = Puzzle()
        p.parse_file_input(file='test_part2')
        result = p.run()
        self.assertEqual('fgij', result)

    def test_answer_2(self):
        p = Puzzle()
        p.parse_file_input(file='input_part_2')
        result = p.run()
        print("Answer is {}".format(result))
        self.assertIsInstance(result, str)
