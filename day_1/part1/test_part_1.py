import unittest
from day_1.part1.puzzle_part_1 import Puzzle


class TestPart1(unittest.TestCase):

    def test_1(self):
        p = Puzzle(current=0)
        p.parse_string_input('+1, -2, +3, +1')
        result = p.run()
        self.assertEqual(result, 3)

    def test_2(self):
        p = Puzzle(current=0)
        p.parse_string_input('+1, +1, +1')
        result = p.run()
        self.assertEqual(result, 3)

    def test_3(self):
        p = Puzzle(current=0)
        p.parse_string_input('+1, +1, -2')
        result = p.run()
        self.assertEqual(result, 0)

    def test_4(self):
        p = Puzzle(current=0)
        p.parse_string_input('-1, -2, -3')
        result = p.run()
        self.assertEqual(result, -6)

    def test_answer_1(self):
        p = Puzzle(current=0)
        p.parse_file_input(file='input_part_1')
        result = p.run()
        print("Answer is {}".format(result))
        self.assertIsInstance(result, int)
