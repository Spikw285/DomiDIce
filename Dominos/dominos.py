#This class will contain only doubles of dominos that are considered as common
class CommonDomino:
        #n/n
    class Doubles:
        def none_none_domino(self):
            pass

        def one_one_domino(self):
            pass

        def two_two_domino(slef):
            pass

        def three_three_domino(self):
            pass

        def four_four_domino(self):
            pass

        def five_five_domino(self):
            pass

        def six_six_domino(self):
            pass

        def seven_seven_domino(self):
            pass

        def eight_eight_domino(self):
            pass

        def nine_nine_domino(self):
            pass
        #n/m
    class Ratios:
        #N/n^2
        class ReversePowerTwo:
            #1/2
            def half_domino(self):
                pass
            #1/4
            def quarter_domino(self):
                pass
            #1/8
            def eight_part_domino(self):
                pass
        #1/3
        def one_third_domino(self):
            pass
        #2/3
        def two_thirds_domino(self):
            pass
        #3/4
        def three_quarter_domino(self):
            pass
        class SuperFives:
            #1/5
            def one_fifth_domino(self):
                pass
            #2/5
            def two_fifth_domino(self):
                pass
            #3/5
            def three_fifth_domino(self):
                pass
            #4/5
            def four_fifth_domino(self):
                pass
            #Following two dominos are considered "cursed" since six is considered "unlucky"
        #1/6
        def cursed_one_six_domino(self):
            pass
        #5/6
        def cursed_five_six_domino(self):
            pass
        class LuckySevens:
            #1/7
            def one_seven_domino(self):
                pass
            #2/7
            def two_seven_domino(self):
                pass
            #3/7
            def three_seven_domino(self):
                pass
            #4/7
            def four_seven_domino(self):
                pass
            #5/7
            def five_seven_domino(self):
                pass
            #6/7
            def six_seven_domino(self):
                pass
        #n/8
        class IncredibleEight:
            def one_eight_domino(self):
                return CommonDomino.Ratios.ReversePowerTwo.eight_part_domino(self)
            #3/8
            def three_eight_domino(self):
                pass
            #5/8
            def five_eight_domino(self):
                pass
            #7/8
            def seven_eight_domino(self):
                pass
        #n/9
        class TheNines:
            #2/9
            def two_nine_domino(self):
                pass
            #4/9
            def four_nine_domino(self):
                pass
            #5/9
            def five_nine_domino(self):
                pass
            #7/9
            def seven_nine_domino(self):
                pass
            #8/9
            def eight_nine_domino(self):
                pass
        #N/n
        class BlankGang:
            def none_one_domino(self):
                pass
            def none_two_domino(self):
                pass
            def none_three_domino(self):
                pass
            def none_four_domino(self):
                pass
            def none_five_domino(self):
                pass
            def none_six_domino(self):
                pass
            def none_seven_domino(self):
                pass
            def none_eight_domino(self):
                pass
            def none_nine_domino(self):
                pass

#This class will contain uncommon types of dominos that are actually from Mahjong
class mahjongUncommonDomino:
    #"copper"
    def tun_domino(self):
        pass
    '''
    This domino has effect of giving some "gold" in random range from 5 to 25 from every table at 40% rate
    '''
    #"bamboo"
    def suo_domino(self):
        pass
    '''
    This domino has effect of giving random chance to give another dice made out of bamboo at 35% chance rate
    '''
    #"darkness"
    def wan_domino(self):
        pass
    '''
    This domino has effect to decrease some amount of required points up to 50% of original every table. It has next chances to decrease at some amount:
    1%-15%: 46% chance
    16%-29%: 25% chance
    30%-39%: 21% chance
    40%-50%: 8% chance
    '''
    class Winds:
        def east_wind_domino(self):
            pass
        '''
        This domino has effect to increase chance of prok chances of other dominos from left up to 25%
        '''
        def south_wind_domino(self):
            pass
        '''
        This domino has effect to increase chance of throwing "highs" up to 35%
        '''
        def west_wind_domino(self):
            pass
        '''
        This domino has effect to increase chance of prok chances of other dominos from right up to 25%
        '''
        def north_wind_domino(self):
            pass
        '''
        This domino has effect to decrease chance of throwing "lows" up to 35%
        '''
    def white_rice_domino(self):
        pass
    '''
    This domino has effect to give additional chance of prok chances of all dominos up to 10%
    '''
    def rooster_domino(self):
        pass
    '''
    This domino has effect to give 
    '''

#This class will contain rare types of dominos that are actually from Mahjong
class mahjongRareDomino:
    class Dragons:
        def red_dragon_domino(self):
            pass
        def greed_dragon_domino(self):
            pass
        def white_dragon_domino(self):
            pass
    class Seasons:
        def spring_domino(self):
            pass
        def summer_domino(self):
            pass
        def autumn_domino(self):
            pass
        def winter_domino(self):
            pass
    class Plants:
        def plum_domino(self):
            pass
        def orchid_domino(self):
            pass
        def chrysantenium_domino(self):
            pass
        def bamboo_domino(self):
            pass

class mahjongLegendaryDomino:
    def black_dragon_domino(self):
        pass
    def white_rabbit_domino(self):
        pass
    def ying_domino(self):
        pass
    def yang_domino(self):
        pass
    def ether_domino(self):
        pass
