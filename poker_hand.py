from result import Result
'''

_hand_arr: array of cards [value][suit]
'''
class PokerHand():
    _hand = ""
    _hand_arr = []

    def __init__(self, hand):
        if type(hand) != str:
            raise TypeError("Invalid type of hand")
        hand_arr = hand.split(" ")
        if len(hand_arr) != 5:
            raise ValueError("Invalid hand size given: ")
        for h in hand_arr:
            pass
            

    def compare_with(self, pokerHand):
        print("hand_A: %s \t hand_B: %s".format(self._hand, pokerHand._hand))
        if(self._hand == pokerHand._hand):
            return Result.WIN
        else:
            return Result.LOSS
    
    def classify_hand():
        pass


if __name__ == "__main__":
    print("PokerHand_test")

