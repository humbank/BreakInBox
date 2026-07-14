class Puzzle:
    def __init__(self, title, description, hints):
        self.title = title
        self.description = description
        self.hints = hints


class laser_puzzle(Puzzle):
    def __init__(self, title, description, hints):
        super().__init__(title, description, hints)

    def setup(self):
        pass

class code_puzzle(Puzzle):
    def __init__(self, title, description, hints, solution):
        super().__init__(title, description, hints)
        self.solution = solution

    def setup(self):
        pass

class test_puzzle(Puzzle):
    def __init__(self, title, description, hints, esps):
        super().__init__(title, description, hints)
        self.esps = esps
