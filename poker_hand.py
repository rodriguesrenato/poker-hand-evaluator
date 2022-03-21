from poker_classifications import Result, PokerRanking
from collections import Counter

'''
A class to classify and compare poker hands
'''
class PokerHand():

    # Conversion dictionaries
    card_value_dict = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    card_suit_dict = {"S": 0, "H": 1, "D": 2, "C": 3}

    # Debug level flag
    _debug_level = 0

    def __init__(self, hand):

        self.hand = hand
        self.hand_cards = []
        self.hand_classification = None
        self.hand_cards_counter = None

        # Check for invalid input
        if type(self.hand) != str:
            raise TypeError("Invalid type of hand")

        hand_arr = self.hand.split(" ")
        if len(hand_arr) != 5:
            raise ValueError("Invalid hand size given: ")

        for h in hand_arr:
            card_value = None
            card_suit = None

            # Get card value
            if(h[:1].isdigit()):
                card_value = int(h[:1])
            else:
                card_value = PokerHand.card_value_dict.get(h[:1])

            # Get card suit
            card_suit = PokerHand.card_suit_dict.get(h[1:2])

            # Check if this card is valid
            if(card_value < 2 and card_suit is not None):
                raise ValueError("Invalid card {}: value = {}, suit = {}".format(
                    h, card_value, card_suit))

            # Add the converted card to the cards list
            self.hand_cards.append((card_value, card_suit))

        # Sort hand by value and suit, from lowest to highest
        self.hand_cards = sorted(self.hand_cards, key=lambda x: (x[0], x[1]))

        # Classify hand 
        self.classify_hand()

        # Debug - Print a detailed report
        if(PokerHand._debug_level > 1):
            self.print_details()

    # Classify hand by PokerRanking enum
    def classify_hand(self):

        is_sequence = True
        is_flush = True

        # Check for a sequence of 5 values and for same suit in all cards (flush)
        for i in range(0, len(self.hand_cards)-1):
            if self.hand_cards[i][0] != (self.hand_cards[i+1][0] - 1):
                is_sequence = False
            if self.hand_cards[i][1] != self.hand_cards[i+1][1]:
                is_flush = False

        # Count cards of same denomination, ordered by the highest value
        cards_counter = Counter(card[0] for card in self.hand_cards)
        self.hand_cards_counter = sorted(
            cards_counter.items(), key=lambda item: (-item[1], -item[0]))

        # Start classifying the poker hand
        if is_sequence:
            if is_flush:
                if self.hand_cards[-1][0] == PokerHand.card_value_dict.get("A"):
                    self.hand_classification = PokerRanking.ROYAL_STRAIGHT_FLUSH
                else:
                    self.hand_classification = PokerRanking.STRAIGHT_FLUSH
            else:
                self.hand_classification = PokerRanking.STRAIGHT
        else:
            if is_flush:
                self.hand_classification = PokerRanking.FLUSH
            else:
                # Check the counter of cards with same denomination
                if(self.hand_cards_counter[0][1] == 4):
                    self.hand_classification = PokerRanking.FOUR_OF_A_KIND
                elif(self.hand_cards_counter[0][1] == 3):
                    if(self.hand_cards_counter[1][1] == 2):
                        self.hand_classification = PokerRanking.FULL_HOUSE
                    else:
                        self.hand_classification = PokerRanking.TREE_OF_A_KIND
                elif(self.hand_cards_counter[0][1] == 2):
                    if(self.hand_cards_counter[1][1] == 2):
                        self.hand_classification = PokerRanking.TWO_PAIR
                    else:
                        self.hand_classification = PokerRanking.ONE_PAIR
                else:
                    self.hand_classification = PokerRanking.HIGH_CARD


    def compare_with(self, other_hand):
        # Debug
        if(PokerHand._debug_level > 0):
            print("[PokerHand.compare_with] Hand \t[{}] ({}){}compared with  [{}] ({}){}".format(
                self.hand, self.hand_classification.name,
                " "*(22-len(self.hand_classification.name)),
                other_hand.hand, other_hand.hand_classification.name,
                " "*(21-len(other_hand.hand_classification.name))), end='')

        # Initialize result as TIE
        result = Result.TIE

        # Compare classifications of both hands
        if(self.hand_classification > other_hand.hand_classification):
            result = Result.WIN
        elif(self.hand_classification < other_hand.hand_classification):
            result = Result.LOSS

        # If classifications are the same, then try to break tie
        else:
            # (Royal) Straight flush or Straight: Compare the highest value of sequences
            if (self.hand_classification == PokerRanking.STRAIGHT_FLUSH
                    or self.hand_classification == PokerRanking.ROYAL_STRAIGHT_FLUSH
                    or self.hand_classification == PokerRanking.STRAIGHT):
                if(self.hand_cards[-1][0] > other_hand.hand_cards[-1][0]):
                    result = Result.WIN
                if(self.hand_cards[-1][0] < other_hand.hand_cards[-1][0]):
                    result = Result.LOSS

            elif (self.hand_classification == PokerRanking.TWO_PAIR):
                # Compare the first highest pair
                if(self.hand_cards_counter[0][0] > other_hand.hand_cards_counter[0][0]):
                    result = Result.WIN
                elif(self.hand_cards_counter[0][0] < other_hand.hand_cards_counter[0][0]):
                    result = Result.LOSS
                else:
                    # Compare the second highest pair
                    if(self.hand_cards_counter[1][0] > other_hand.hand_cards_counter[1][0]):
                        result = Result.WIN
                    elif(self.hand_cards_counter[1][0] < other_hand.hand_cards_counter[1][0]):
                        result = Result.LOSS
                    else:
                        # Compare the fifth card
                        if(self.hand_cards_counter[2][0] > other_hand.hand_cards_counter[2][0]):
                            result = Result.WIN
                        elif(self.hand_cards_counter[2][0] < other_hand.hand_cards_counter[2][0]):
                            result = Result.LOSS

            elif (self.hand_classification == PokerRanking.ONE_PAIR):
                # Compare pairs
                if(self.hand_cards_counter[0][0] > other_hand.hand_cards_counter[0][0]):
                    result = Result.WIN
                elif(self.hand_cards_counter[0][0] < other_hand.hand_cards_counter[0][0]):
                    result = Result.LOSS
                else:
                    # As pairs are the same, then look for the highest card of the 3 cards left, compared one to one on a ordered sequence
                    for i in range(1, 4):
                        if(self.hand_cards_counter[i][0] > other_hand.hand_cards_counter[i][0]):
                            result = Result.WIN
                            break
                        elif(self.hand_cards_counter[i][0] < other_hand.hand_cards_counter[i][0]):
                            result = Result.LOSS
                            break

            elif (self.hand_classification == PokerRanking.HIGH_CARD):
                # Look for the highest card of both hands, ordered by the highest value and checked one by one on sequence, skipping when both have same value
                for i in range(0, 5):
                    if(self.hand_cards_counter[i][0] > other_hand.hand_cards_counter[i][0]):
                        result = Result.WIN
                        break
                    elif(self.hand_cards_counter[i][0] < other_hand.hand_cards_counter[i][0]):
                        result = Result.LOSS
                        break

            # Four of a kind: Compare the value of both hand, can't be the same value
            # Full house: Compare the value of the tree of a kind on both hand, can't be the same value
            # Flush: Compare the highest value card of both flush hand
            # Three of a kind: Compare the value of the tree of a kind on both hand, can't be the same value
            else:
                if(self.hand_cards_counter[0][0] > other_hand.hand_cards_counter[0][0]):
                    result = Result.WIN
                else:
                    result = Result.LOSS

        # Debug result
        if(PokerHand._debug_level > 0):
            print("-> Result: ", result.name)

        return result


    # Print a detailed report of the processed poker hand given
    def print_details(self):
        # Auxiliar formatting Print vars
        print_header = "[PokerHand.print_details]"
        print_header_tab = " "*len(print_header)

        # Print the hand string received as input
        print("{} String hand received: {}".format(
            print_header, self.hand))

        # Print the list of cards
        print("{} Cards (value,suit):".format(print_header_tab))
        for c in self.hand_cards:
            print("{}\t{}".format(print_header_tab, c))

        # Print the list of card value followed by its number of occurences
        print("{} Cards counter (value,value_count): ".format(print_header_tab))
        for c in self.hand_cards_counter:
            print("{}\t{}".format(print_header_tab, c))

        # Print the final classification
        print("{} Classification: {}".format(
            print_header_tab, self.hand_classification.name))
