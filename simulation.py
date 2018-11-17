#!/usr/bin/python3
from copy import deepcopy
from random import shuffle

SUITS=('C', 'H','S','D')
VALUES=('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
VALUE_VALUES={
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':5,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14,
}
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
ROYAL_FLUSH = 1
STRAIGHT_FLUSH = 2
FOUR_KIND = 3
FULL_HOUSE = 4
FLUSH = 5
STRAIGHT = 6
THREE_KIND = 7
TWO_PAIR = 8
PAIR = 9
HIGH_CARD = 10
HAND_RANKS = {
    ROYAL_FLUSH: 'Royal Flush',
    STRAIGHT_FLUSH: 'Straight Flush',
    FOUR_KIND: 'Four of a Kind',
    FULL_HOUSE: 'Full House',
    FLUSH: 'Flush',
    STRAIGHT: 'Straight',
    THREE_KIND: 'Three of a Kind',
    TWO_PAIR: 'Two Pair',
    PAIR: 'Pair',
    HIGH_CARD: 'High Card',
}

DELIM=','

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
    counts = {}
    for card in hand:
        if card[0] in counts:
            counts[card[0]] += 1
        else:
            counts[card[0]] = 1

    return (4 in counts.values())

def is_full_house(hand):
    counts = {}
    for card in hand:
        if card[0] in counts:
            counts[card[0]] += 1
        else:
            counts[card[0]] = 1

    return (2 in counts.values() and 3 in counts.values())

def is_flush(hand):
    val, suit = zip(*hand)
    if (len(set(suit)) == 1):
        return True
    return False

def is_straight(hand):
    val, suit = zip(*hand)
    if (set(val) in STRAIGHTS):
        return True
    return False

def is_three_of_a_kind(hand):
    counts = {}
    for card in hand:
        if card[0] in counts:
            counts[card[0]] += 1
        else:
            counts[card[0]] = 1

    for score in counts:
        if (counts[score] == 3):
            return True
    return False

def is_two_pair(hand):
    counts = {}
    for card in hand:
        if card[0] in counts:
            counts[card[0]] += 1
        else:
            counts[card[0]] = 1

    pairs = 0
    for count in counts:
        if (counts[count]==2):
            pairs+=1

    return (pairs==2)

def is_pair(hand):
    counts = {}
    for card in hand:
        if card[0] in counts:
            counts[card[0]] += 1
        else:
            counts[card[0]] = 1

    pairs = 0
    for count in counts:
        if (counts[count] == 2):
            pairs += 1

    return (pairs == 1)

def get_hand_rank(hand):
    if(is_royal_flush(hand)):
        return ROYAL_FLUSH
    elif(is_straight_flush(hand)):
        return STRAIGHT_FLUSH
    elif(is_four_of_a_kind(hand)):
        return FOUR_KIND
    elif(is_full_house(hand)):
        return FULL_HOUSE
    elif(is_flush(hand)):
        return FLUSH
    elif(is_straight(hand)):
        return STRAIGHT
    elif(is_three_of_a_kind(hand)):
        return THREE_KIND
    elif(is_two_pair(hand)):
        return TWO_PAIR
    elif(is_pair(hand)):
        return PAIR
    else:
        return HIGH_CARD

def shuffled_deck():
    d = deepcopy(deck)
    shuffle(d)
    return d
    

def deal_hand():
    d = shuffled_deck()
    return d[0:5]

def deal_hand_from_deck(d):
    return d[0:5]

if (__name__=='__main__'):
    
    # Get shuffled deck
    d = shuffled_deck()
    
    counts = [0,0,0,0,0,0,0,0,0,0]
    iterations = 10000000
    display_at=100
    print('Iteration%sRoyal Flush%sStraight Flush%s4 of a Kind%sFull House%sFlush%sStraight%s3 of a Kind%s 2 Pair%sPair%sHigh Card'%(DELIM,
                                                                                                                                     DELIM,
                                                                                                                                     DELIM,
                                                                                                                                     DELIM,
                                                                                                                                     DELIM,
                                                                                                                                     DELIM,
                                                                                                                                     DELIM,
                                                                                                                                     DELIM,
                                                                                                                                     DELIM,
                                                                                                                                     DELIM))
    for i in range(1,iterations+1):
        shuffle(d)
        hand=deal_hand_from_deck(d)
        counts[get_hand_rank(hand)-1] += 1 

        if (i == display_at):
            print(i, end=DELIM)
            for j in counts:
                print(j, end=DELIM)
            print()
            display_at*=10

    print('Final Count:')
    print(i, end=DELIM)
    for j in counts:
        print(j, end=DELIM)
    print()


    print('chance', end=DELIM)
    for j in counts:
        print(float(j/iterations), end=DELIM)

    print('\nDone.')
