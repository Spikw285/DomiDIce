import random


class DiceRolls:
    def roll_dice(self, sides):
        return random.randint(1, sides)

    def d2Roll(self):
        return self.roll_dice(2)

    def d4Roll(self):
        return self.roll_dice(4)

    def d6Roll(self):
        return self.roll_dice(6)

    def d8Roll(self):
        return self.roll_dice(8)

    def d10Roll(self):
        return self.roll_dice(10)

    def d12Roll(self):
        return self.roll_dice(12)

    def d20Roll(self):
        return self.roll_dice(20)

    def dPercentRoll(self):
        return self.roll_dice(100)
