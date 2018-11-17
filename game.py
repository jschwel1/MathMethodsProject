import simulation

def comp_hands(hand1, hand2):
    """ comp_hands(hand1, hand2)
    parameters
    hand1: 5 cards given to one player
    hand2: 5 cards given to another player
    
    returns
    -1: hand1 is better
     0: tie
     1: hand2 is better
    """
    H1_WINS = -1
    H2_WINS = 1
    TIE = 0

    type1 = get_hand_rank(hand1) 
    type2 = get_hand_rank(hand2) 
    h1v, h1s - zip(*hand1)
    h1vals = [simulation.VALUE_VALUES[x] for x in h1v]
    h2v, h2s - zip(*hand2)
    h2vals = [simulation.VALUE_VALUES[x] for x in h2v]

    if (type1 == type2):
        if (type1 == ROYAL_FLUSH):
            return TIE
        elif (type1 == STRAIGHT_FLUSH):
            if (max(h1vals] > max(h2vals)):
                return H1_WINS
            elif (max(h1vals] < max(h2vals)):
                return H2_WINS
            else:
                return TIE
        elif (type1 == FOUR_KIND):
            if(h1vals[0] > h2vals[0]):
                return H1_WINS
            elif(h1vals[0] < h2vals[0]):
                return H2_WINS
            else:
                return TIE
        elif (type1 == FLUSH):
        elif (type1 == STRAIGHT):
        elif (type1 == THREE_KIND):
        elif (type1 == TWO_PAIR):
        elif (type1 == PAIR):
        elif (type1 == HIGH_CARD):
    return -1 if (type1 < type2) else 1
