import itertools


class Puzzle:

    def __init__(self, current: int) -> None:
        self.current = current
        self.movements = []
        self.results = set()
        self.results.add(current)

    def run(self) -> int:
        for movement in itertools.cycle(self.movements):
            self.current += int(movement)
            if self.current in self.results:
                break
        return self.current

    def parse_string_input(self, input_string: str) -> None:
        self.movements = input_string.split(',')

    def parse_file_input(self, file: str) -> None:
        with open(file) as f:
            lines = f.read().splitlines()
        self.movements = lines
