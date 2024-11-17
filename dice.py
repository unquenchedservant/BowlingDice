import random
class Dice:
    def __init__(self, type):
        self.type = type
        self.active = True
        self.result = "standing"

    def roll(self):
        # get random number between 1 and 6
        result=random.randint(1,6)
        if result == 6:
            if self.type == "regular":
                self.result = "down"
            elif self.type == "strike":
                self.result = "strike"
            elif self.type == "spare":
                self.result = "spare"
    