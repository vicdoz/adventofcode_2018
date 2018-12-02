class Puzzle:

    def __init__(self) -> None:
        self.lines = []

    def run(self) -> int:
        two_ocurrences = 0
        three_ocurrences = 0
        for line in self.lines:
            ocurrences = {}
            for char in line:
                ocurrences[line.count(char)] = char
            two_ocurrences = self.find_ocurrences(2, ocurrences, two_ocurrences)
            three_ocurrences = self.find_ocurrences(3, ocurrences, three_ocurrences)

        result = three_ocurrences * two_ocurrences

        return result

    def find_ocurrences(self, char, ocurrences, counter):
        if char in ocurrences:
            counter += 1
        return counter

    def parse_file_input(self, file: str) -> None:
        with open(file) as f:
            lines = f.read().splitlines()
        self.lines = lines
