# poker-hand-evaluator

A python class to evaluate and compare poker hands.

This project solution was developed for the [`Data H - Python Challenge`](desafio_python_v1_0.pdf).

# Dependencies

This project was developed and run on Ubuntu 20.04 LTS. The following dependencies/modules were used:

- Python 3.8.10
- Python built-in modules:
    - collections
    - enum
    - unittest

# Installation

Clone this repository

```bash
git clone https://github.com/rodriguesrenato/poker-hand-evaluator.git
```

# Usage

The Python Challenge tests can be executed by running the following command in the terminal, on the `poker-hand-evaluator` folder:

```bash
python3 test_hands_evaluation.py
```

Here is the output of the unit tests (with `debug_level` set as 1):

!["Unit Tests"](images/test_results.png)

The `PokerHand` class can be directly imported in your own solution. The `PokerRanking` class has the predefined poker hand classifications and `PokerResult` class has the possible comparison results between two hands.

```python
from poker_hand import PokerHand, PokerRanking, PokerResult
```

# Solution

The solution for this challenge was developed in the class `PokerHand` and it has two auxiliary classes (`PokerRanking` and `PokerResult`) of enumerators to classify the hand ranking and hand comparison result.

The `PokerHand` class has the following structure:

```
PokerHand
    | __init__()
    | classify_hand()
    | compare_with()
    | print_details()
```

A `PokerHand` object must be instantiated with a string of five cards, separated by a single space. Each card is composed of two digits: the card value and suit.

### Instantiation
 
The `__init__` method checks if the given string of five cards has five valid cards, in order to convert it into a list of numeric tuples of each card value and suit. The non numerical card values and suits are converted to numbers accordingly to a predefined dictionaries:
 
```python
# Conversion dictionaries
card_value_dict = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
card_suit_dict = {"S": 0, "H": 1, "D": 2, "C": 3}
```
 
This list is ordered by the card value, from lowest to highest value. It is stored in the `hand_cards` object data attribute. Here is an example of a instantiated hand:
 
```
Poker hand string:              JH JD TH TC 4C
 
Converted hand (value,suit):    (4, 3)
                               (10, 1)
                               (10, 3)
                               (11, 1)
                               (11, 2)
```
 
Finally, the given hand rating is classified by the `classify_hand()` member function, 

### Poker Hand classification

The `classify_hand()` member function classifies the object list of cards in the ratings defined in the `PokerRanking` class, according to the **Poker Hand Value Ratings**.

!["Poker Hand Ratings](images/poker_ratings.png)

The strategy that was chosen to classify the poker hand was to first check for a full sequence of values (`is_sequence`) and a flush - same suit for all cards - (`is_flush`), and then create a list of unique card values and its respective number of cards with same value in the poker hand (`hand_cards_counter`), in descending order of value quantities.

The classification result is stored in the `hand_classification` data attribute.

### Poker hands comparison

The `compare_with()` member function compares the current object hand with the given hand from other PokerHand object

The comparison starts with a simple check between `hand_classification` and then, if they are the same, it tries to break ties by following the Texas Hold'em rules.

It will return an object of `PokerResult`, which can be `WIN`, `LOSS` or `TIE`.

## Debug

A print function was implemented to assist the development and debug of the solution. The `_debug_level` PokerHand member attribute defines how much information will be shown in the output:

| _debug_level | Information |
|---|---|
| 0 | Debug off (Default)|
| 1 | PokerHand comparison result|
| greater or equal 2 | Initialized hand details and classification, and PokerHand comparison result |

# License 

The contents of this repository are covered under the MIT License.

# References

- Tie break rules: https://pokerdicas.com/regras/regras-de-desempate-no-texas-holdem/