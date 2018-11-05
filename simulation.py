SUITS=('C', 'H','S','D')
VALUES=('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
STRAIGHTS=({'A', '2', '3', '4', '5'},
           {'2', '3', '4', '5', '6'},
           {'3', '4', '5', '6', '7'},
           {'4', '5', '6', '7', '8'},
           {'5', '6', '7', '8', '9'},
           {'6', '7', '8', '9', '10'},
           {'7', '8', '9', '10', 'J'},
           {'8', '9', '10', 'J', 'Q'},
           {'9', '10', 'J', 'Q', 'K'},
           {'10', 'J', 'Q', 'K', 'A'},)
deck = [(val, suit) for val in VALUES for suit in SUITS]

def is_royal_flush(hand):
    vals, suits = zip(*hand)
    if (len(set(suits)) > 1):
        return False # more than 1 suit
    if (set(vals) == {'A', 'K', 'Q', 'J', '10'}):
        return True
    return False

def is_straight_flush(hand):
    vals, suits = zip(*hand)
    if (len(set(suits)) > 1):
        return False # more than 1 suit
    if (set(vals) in STRAIGHTS):
        return True
    return False

def is_four_of_a_kind(hand):
    pass

def is_full_house(hand):
    pass

def is_flush(hand):
    pass

def is_straight(hand):
    pass

def is_three_of_a_kind(hand):
    pass

def is_two_pair(hand):
    pass

def is_pair(hand):
    pass