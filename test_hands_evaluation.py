import unittest
import argparse
from poker_hand import PokerHand, PokerRanking, PokerResult

class TestMethods(unittest.TestCase):
    # Hand classification test
    def test_classify_hand(self):
        self.assertTrue(
            PokerHand("AC KC QC JC TC").hand_classification == PokerRanking.ROYAL_STRAIGHT_FLUSH)
        self.assertTrue(
            PokerHand("5H 6H 7H 8H 9H").hand_classification == PokerRanking.STRAIGHT_FLUSH)
        self.assertTrue(
            PokerHand("TS TH TD TC QH").hand_classification == PokerRanking.FOUR_OF_A_KIND)
        self.assertTrue(
            PokerHand("QS QC QH 5D 5C").hand_classification == PokerRanking.FULL_HOUSE)
        self.assertTrue(
            PokerHand("KH TH 7H 6H 3H").hand_classification == PokerRanking.FLUSH)
        self.assertTrue(
            PokerHand("4S 5H 6D 7C 8S").hand_classification == PokerRanking.STRAIGHT)
        self.assertTrue(
            PokerHand("7S 7H 7D AS 9S").hand_classification == PokerRanking.TREE_OF_A_KIND)
        self.assertTrue(
            PokerHand("AS AH 6C 6D 2H").hand_classification == PokerRanking.TWO_PAIR)
        self.assertTrue(
            PokerHand("KS KH AC 7C 4H").hand_classification == PokerRanking.ONE_PAIR)
        self.assertTrue(
            PokerHand("QC 5S 2H 7D 8C").hand_classification == PokerRanking.HIGH_CARD)

    # Hands comparison tests
    def test_compare_hands(self):
        self.assertTrue(PokerHand("TC TH 5C 5H KH").compare_with(
            PokerHand("TC TH 5C 5H KH")) == PokerResult.TIE)
        self.assertTrue(PokerHand("TC TH 5C 5H KH").compare_with(
            PokerHand("9C 9H 5C 5H AC")) == PokerResult.WIN)
        self.assertTrue(PokerHand("TS TD KC JC 7C").compare_with(
            PokerHand("JS JC AS KC TD")) == PokerResult.LOSS)
        self.assertTrue(PokerHand("7H 7C QC JS TS").compare_with(
            PokerHand("7D 7C JS TS 6D")) == PokerResult.WIN)
        self.assertTrue(PokerHand("5S 5D 8C 7S 6H").compare_with(
            PokerHand("7D 7S 5S 5D JS")) == PokerResult.LOSS)
        self.assertTrue(PokerHand("AS AD KD 7C 3D").compare_with(
            PokerHand("AD AH KD 7C 4S")) == PokerResult.LOSS)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(
            PokerHand("AC AH AS AS KS")) == PokerResult.WIN)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(
            PokerHand("TC JS QC KS AC")) == PokerResult.WIN)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(
            PokerHand("QH QS QC AS 8H")) == PokerResult.WIN)
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(
            PokerHand("TC JS QC KS AC")) == PokerResult.WIN)
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(
            PokerHand("QH QS QC AS 8H")) == PokerResult.WIN)
        self.assertTrue(PokerHand("TC JS QC KS AC").compare_with(
            PokerHand("QH QS QC AS 8H")) == PokerResult.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(
            PokerHand("JH JC JS JD TH")) == PokerResult.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(
            PokerHand("4H 5H 9H TH JH")) == PokerResult.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(
            PokerHand("7C 8S 9H TH JH")) == PokerResult.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(
            PokerHand("TS TH TD JH JD")) == PokerResult.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(
            PokerHand("JH JD TH TC 4C")) == PokerResult.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(
            PokerHand("4H 5H 9H TH JH")) == PokerResult.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(
            PokerHand("7C 8S 9H TH JH")) == PokerResult.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(
            PokerHand("TS TH TD JH JD")) == PokerResult.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(
            PokerHand("JH JD TH TC 4C")) == PokerResult.WIN)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(
            PokerHand("7C 8S 9H TH JH")) == PokerResult.WIN)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(
            PokerHand("TS TH TD JH JD")) == PokerResult.LOSS)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(
            PokerHand("JH JD TH TC 4C")) == PokerResult.WIN)
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(
            PokerHand("TS TH TD JH JD")) == PokerResult.LOSS)
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(
            PokerHand("JH JD TH TC 4C")) == PokerResult.WIN)
        self.assertTrue(PokerHand("TS TH TD JH JD").compare_with(
            PokerHand("JH JD TH TC 4C")) == PokerResult.WIN)


if __name__ == '__main__':
    PokerHand._debug_level = 1
    unittest.main()
