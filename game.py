import hand

class Game:
    def __init__(self):
        self.hand = hand.Hand()
        self.points = 0
        self.frame = 1
        self.framePos = 1
        self.previousResult = "normal"
        self.prevScore = 0

    def play(self):
        pass
    