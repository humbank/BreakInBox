from comm import *

class Puzzle:
    def __init__(self, title, descriptions, hints):
        self.title = title
        self.descriptions = descriptions
        self.hints = hints


class laser_puzzle(Puzzle):
    def __init__(self, title, descriptions, hints):
        super().__init__(title, descriptions, hints)

    def setup(self):
        pass

class code_puzzle(Puzzle):
    def __init__(self, title, descriptions, hints, solution):
        super().__init__(title, descriptions, hints)
        self.solution = solution

    def setup(self):
        pass

class test_puzzle(Puzzle):
    def __init__(self, title, descriptions, hints, esps):
        super().__init__(title, descriptions, hints)
        self.esps = esps
    
    def set_availability(self):
        for esp in self.esps:
            send("wake", esp.id)
    
    def setup(self, window):
        self.set_availability()
        window.pb_led1_on.clicked.connect(lambda: self.esps[0].one.led_on())
        window.pb_led1_off.clicked.connect(lambda: self.esps[0].one.led_off())
        window.pb_led2_on.clicked.connect(lambda: self.esps[0].two.led_on())
        window.pb_led2_off.clicked.connect(lambda: self.esps[0].two.led_off())
