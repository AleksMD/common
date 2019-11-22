
class Room:
    def __init__(self, number, level, price,  status='open'):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


rooms_storage = [Room(3, 'Econom', 1000), Room(1, 'Business', 2000, 'closed')]
