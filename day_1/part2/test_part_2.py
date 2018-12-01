import unittest
from day_1.part2.puzzle_part_2 import Puzzle


class TestPart2(unittest.TestCase):

    def test_2_1(self):
        p = Puzzle(current=0)
        p.parse_string_input('+1, -1')
        result = p.run()
        self.assertEqual(0, result)

    def test_2_1_1(self):
        p = Puzzle(current=0)
        p.parse_string_input('+1,-2,+3,+1')
        result = p.run()
        self.assertEqual(2, result)

    def test_2_2(self):
        p = Puzzle(current=0)
        p.parse_string_input('+3, +3, +4, -2, -4')
        result = p.run()
        self.assertEqual(10, result)

    def test_2_3(self):
        p = Puzzle(current=0)
        p.parse_string_input('-6, +3, +8, +5, -6')
        result = p.run()
        self.assertEqual(5, result)

    def test_2_4(self):
        p = Puzzle(current=0)
        p.parse_string_input('+7, +7, -2, -7, -4')
        result = p.run()
        self.assertEqual(14, result)

    def test_answer_2(self):
        p = Puzzle(current=0)
        p.parse_file_input(file='input_part_2')
        result = p.run()
        print("Answer is {}".format(result))
        self.assertIsInstance(result, int)
