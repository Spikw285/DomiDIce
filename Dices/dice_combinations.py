import random
from collections import Counter

class YahtzeePlus:
    def __init__(self):
        self.combinations = {
            'chance': self.chance,
            'pair': self.pair,
            'two_pairs': self.two_pairs,
            'three_of_a_kind': self.three_of_a_kind,
            'four_of_a_kind': self.four_of_a_kind,
            'three_pairs': self.three_pairs,
            'full_house': self.full_house,
            'small_straight': self.small_straight,
            'medium_straight': self.medium_straight,
            'large_straight': self.large_straight,
            'five_of_a_kind': self.five_of_a_kind,
            'yahtzee': self.yahtzee
        }

    def chance(self, dice):
        return sum(dice)

    def pair(self, dice):
        pairs = [d for d in set(dice) if dice.count(d) >= 2]
        if pairs:
            return max(pairs) * 2 * 1.5
        return 0

    def two_pairs(self, dice):
        pairs = [d for d in set(dice) if dice.count(d) >= 2]
        if len(pairs) >= 2:
            pairs.sort(reverse=True)
            return sum(pairs[:2]) * 2 * 2
        return 0

    def three_of_a_kind(self, dice):
        for d in set(dice):
            if dice.count(d) >= 3:
                return d * 3 * 3
        return 0

    def four_of_a_kind(self, dice):
        for d in set(dice):
            if dice.count(d) >= 4:
                return d * 4 * 4
        return 0

    def three_pairs(self, dice):
        pairs = [d for d in set(dice) if dice.count(d) >= 2]
        if len(pairs) >= 3:
            pairs.sort(reverse=True)
            return sum(pairs[:3]) * 2.5
        return 0

    def full_house(self, dice):
        unique_dice = set(dice)
        if len(unique_dice) == 2 and any(dice.count(d) == 3 for d in unique_dice):
            return 25 * 3
        return 0

    def small_straight(self, dice):
        sorted_dice = sorted(set(dice))
        straights = [
            {1, 2, 3, 4},
            {2, 3, 4, 5},
            {3, 4, 5, 6},
            {4, 5, 6, 7},
            {5, 6, 7, 8},
            {6, 7, 8, 9},
            {7, 8, 9, 10},
            {8, 9, 10, 11},
            {9, 10, 11, 12},
            {10, 11, 12, 13},
            {11, 12, 13, 14},
            {12, 13, 14, 15},
            {13, 14, 15, 16},
            {14, 15, 16, 17},
            {15, 16, 17, 18},
            {16, 17, 18, 19},
            {17, 18, 19, 20}
        ]
        if any(straight <= set(sorted_dice) for straight in straights):
            return sum(dice) * 5
        return 0

    def medium_straight(self, dice):
        sorted_dice = sorted(set(dice))
        straights = [
            {1, 2, 3, 4, 5},
            {2, 3, 4, 5, 6},
            {3, 4, 5, 6, 7},
            {4, 5, 6, 7, 8},
            {5, 6, 7, 8, 9},
            {6, 7, 8, 9, 10},
            {7, 8, 9, 10, 11},
            {8, 9, 10, 11, 12},
            {9, 10, 11, 12, 13},
            {10, 11, 12, 13, 14},
            {11, 12, 13, 14, 15},
            {12, 13, 14, 15, 16},
            {13, 14, 15, 16, 17},
            {14, 15, 16, 17, 18},
            {15, 16, 17, 18, 19},
            {16, 17, 18, 19, 20}
        ]
        if any(straight <= set(sorted_dice) for straight in straights):
            return sum(dice) * 5.5
        return 0

    def large_straight(self, dice):
        sorted_dice = sorted(set(dice))
        straights = [
            {1, 2, 3, 4, 5, 6},
            {2, 3, 4, 5, 6, 7},
            {3, 4, 5, 6, 7, 8},
            {4, 5, 6, 7, 8, 9},
            {5, 6, 7, 8, 9, 10},
            {6, 7, 8, 9, 10, 11},
            {7, 8, 9, 10, 11, 12},
            {8, 9, 10, 11, 12, 13},
            {9, 10, 11, 12, 13, 14},
            {10, 11, 12, 13, 14, 15},
            {11, 12, 13, 14, 15, 16, 17},
            {12, 13, 14, 15, 16, 17, 18},
            {13, 14, 15, 16, 17, 18, 19},
            {14, 15, 16, 17, 18, 19, 20}
        ]
        if any(straight <= set(sorted_dice) for straight in straights):
            return sum(dice) * 6
        return 0

    def five_of_a_kind(self, dice):
        for d in set(dice):
            if dice.count(d) >= 5:
                return d * 5 * 6
        return 0

    def yahtzee(self, dice):
        if len(set(dice)) == 1:
            return sum(dice) * 10
        return 0

    def calculate_score(self, dice, color, d1=None, d2=None, d3=None):
        if color == 'green':
            base_score = self.calculate_green_score(dice)
            if d1:
                base_score = self.apply_domino_effect(base_score, d1)
            return base_score
        elif color == 'orange':
            base_score = self.calculate_orange_score(dice)
            if d2:
                base_score = self.apply_domino_effect(base_score, d2)
            return base_score
        elif color == 'purple':
            base_score = self.calculate_purple_score(dice)
            if d3:
                base_score = self.apply_domino_effect(base_score, d3)
            return base_score

    def calculate_green_score(self, dice):
        scores = [self.combinations[combo](dice) for combo in self.combinations]
        return max(scores)

    def calculate_orange_score(self, dice):
        limited_combinations = ['chance', 'pair', 'three_of_a_kind']
        scores = [self.combinations[combo](dice) for combo in limited_combinations]
        return max(scores)

    def calculate_purple_score(self, dice):
        scores = [self.combinations[combo](dice) for combo in self.combinations]
        return max(scores)

    def apply_domino_effect(self, score, domino):
        if domino['type'] == 'addition':
            return score + domino['value']
        elif domino['type'] == 'multiplication':
            return score * domino['value']
        return score

'''
def yachtCombinations(self):
    pass

def zonkCombinations(self):
    pass

def boBingCombinations(self):
    pass
'''
