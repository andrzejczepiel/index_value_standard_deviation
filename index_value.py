import math

class VolMove:
    def __init__(self, vix: int=0, index: int=0, days: int=0):
        self.vix = vix
        self.index = index
        self.days = days


    def predicted_move(self):
        predicted_move = (self.index * (self.vix / 100) * math.sqrt(self.days / 365))
        return predicted_move




today = VolMove(28, 3050, 50)


print(today.predicted_move())
