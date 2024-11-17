import dice

class Hand:
    def __init__(self):
        self.dice = []
        self.dice.append(dice.Dice("regular"))
        self.dice.append(dice.Dice("regular"))
        self.dice.append(dice.Dice("regular"))
        self.dice.append(dice.Dice("regular"))
        self.dice.append(dice.Dice("strike"))
        self.dice.append(dice.Dice("strike"))
        self.dice.append(dice.Dice("strike"))
        self.dice.append(dice.Dice("spare"))
        self.dice.append(dice.Dice("spare"))
        self.dice.append(dice.Dice("spare"))

    def roll(self, framePos=1):
        if framePos == 1:
            for d in self.dice:
                d.active = True
                d.roll(framePos)
        if framePos == 2:
            for d in self.dice:
                if d.active:
                    d.roll(framePos)