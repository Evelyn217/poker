class PokerHand(object):
    CARD = "23456789TJQKA"
    RESULT = ["Loss", "Tie", "Win"]

    def __init__(self, Black):
        values = ''.join(sorted(Black[::3], key=self.CARD.index))
        #判断是否同花
        suits = set(Black[1::3])
        is_flush = len(suits) == 1
        #是否为顺子
        is_straight = values in self.CARD
        self.score = (2 * sum(values.count(card) for card in values) #不同卡牌计数
                      + 13 * is_straight + 14 * is_flush, #顺子*13，同花*15
                      [self.CARD.index(card) for card in values[::-1]])

    def compare_with(self, White):
         return self.RESULT[(self.score > White.score) - (self.score < White.score) + 1]


##test
#hand,other = "2H 3H 4H 5H 6H" , "KS AS TS QS JS"
Black = input("enter a poker hand: ")
White = input("enter another poker hand: ")
player, opponent = PokerHand(Black), PokerHand(White)
print('Black %s' % player.compare_with(opponent))

