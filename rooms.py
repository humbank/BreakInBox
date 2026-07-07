rooms = {
    "Python Room":{"room_total":5},
    "C Room":{"room_total":3},
    "Java Room":{"room_total":8},
    "Test_puzzle":{"room_total":2, "descriptions":["This is a test romm", "This is thbe end of the test rookm"], "hints":{"hint1":"test", "hint2":"test2"}}
}

class Room():
    def __init__(self, name, room_total, descriptions, hints, total_time=60, required_deletes=[]):
        self.name = name
        self.room_total = room_total
        self.descriptions = descriptions
        self.hints = hints
        self.total_time = total_time
        self.required_deletes = required_deletes
