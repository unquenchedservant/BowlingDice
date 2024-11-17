import random
class Dice:
    def __init__(self, type):
        self.type = type # 3 types, regular, strike, spare
        self.active = True # if dice is active or not (strike, spare, down)
        self.result = "standing" # 4 results, standing, down, strike, spare

    def roll(self, framePos=1):
        # get random number between 1 and 6
        result=random.randint(1,6)
    
        if result == 1 or result == 2 or result == 3:
            self.result = "standing"
        elif result == 4 or result == 5:
            self.result = "down"
            self.active = False
        elif result == 6:
            if self.type == "regular":
                self.result = "down"
                self.active = False
            elif self.type == "strike":
                if framePos == 1:
                    self.result = "strike"
                else:
                    self.result = "down"
                self.active = False
            elif self.type == "spare":
                if framePos == 1:
                    self.result = "down"
                else:
                    self.result = "spare"
                self.active = False
        
    
    def get_result(self):
        return self.result