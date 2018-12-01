class Puzzle:
    current = 0
    movements = []

    def __init__(self, current: int) -> None:
        self.current = current

    def run(self) -> int:
        for movement in self.movements:
            self.current += int(movement)
        return self.current

    def parse_string_input(self, input_string: str) -> None:
        self.movements = input_string.split(',')

    def parse_file_input(self, file: str):
        with open(file) as f:
            lines = f.read().splitlines()
        self.movements = lines
