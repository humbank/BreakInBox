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

