from enum import Enum, IntEnum, auto


class Result(Enum):
    LOSS = 0
    WIN = 1
    TIE = 2


class PokerRanking(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    TREE_OF_A_KIND = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    STRAIGHT_FLUSH = auto()
    ROYAL_STRAIGHT_FLUSH = auto()
