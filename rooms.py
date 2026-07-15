rooms = {
    "Python Room":{"room_total":5},
    "C Room":{"room_total":3},
    "Java Room":{"room_total":8},
    "Test_puzzle":{"room_total":2, "descriptions":["This is a test romm", "This is thbe end of the test rookm"], "hints":{"hint1":"test", "hint2":"test2"}}
}

class Room:
    def __init__(self, name, room_total, puzzles, total_time=60):
        self.name = name
        self.room_total = room_total
        self.current_puzzle_nbr = 1
        self.total_time = total_time
        self.puzzles = puzzles
        self.window = None
    
    def setup(self, window):
        self.window = window
        self.window.pb_puzzle_back.clicked.connect(lambda: self.window.stackedWidget.setCurrentWidget(self.window.page_menu))
        self.update_labels()

        for puzzle in self.puzzles:
            puzzle.setup(self.window)
    

    def next_puzzle(self):
        self.current_puzzle_nbr += 1
        self.update_labels
    
    def update_labels(self):
        self.window.lbl_puzzle_nbr.setText(f'{self.current_puzzle_nbr}/{self.room_total}')
        self.window.lbl_puzzle_descr.setText(self.puzzles[self.current_puzzle_nbr-1].descriptions[self.current_puzzle_nbr-1])
