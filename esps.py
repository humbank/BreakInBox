from comm import send


class ESP():
    def __init__(self, name, id):
        self.name = name
        ##self. assets = assets
        self.id = id
        self.one = one(1)
        self.two = two(2)



class one():
    def __init__(self, id):
        self.id = id
    
    def led_on(self):
        send("led_on", self.id)

    def led_off(self):
        send("led_off", self.id)


class two():
    def __init__(self, id):
        self.id = id
    
    def led_on(self):
        send("led_on", self.id)

    def led_off(self):
        send("led_off", self.id)