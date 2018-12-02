from collections import Counter


class Puzzle:

    def __init__(self) -> None:
        self.lines = []
        self.appears = {}

    def parse_file_input(self, file: str) -> None:
        with open(file) as f:
            lines = f.read().splitlines()
        self.lines = lines

    def run(self) -> str:
        sets = Counter()

        for line in self.lines:
            for char in range(len(line)):
                current = tuple(line[:char] + "*" + line[(char + 1):])
                sets[current] += 1

        [(common_string, characters_in_common)] = sets.most_common(1)
        result = "".join([char for char in common_string if char != "*"])
        return result
