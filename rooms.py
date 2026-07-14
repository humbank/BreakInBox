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
        self.total_time = total_time
        self.puzzles = puzzles
    
    def setup(self, window, current_room_nbr):
        window.pb_puzzle_back.clicked.connect(lambda: window.stackedWidget.setCurrentWidget(window.page_menu))
        window.lbl_puzzle_nbr.setText(f'{current_room_nbr}/{self.room_total}')
        window.lbl_puzzle_descr.setText(self.puzzles[current_room_nbr-1].descriptions[current_room_nbr-1])

        for puzzle in self.puzzles:
            puzzle.setup(window)

