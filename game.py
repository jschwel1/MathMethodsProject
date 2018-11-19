#!/usr/bin/python3
import simulation
import numpy as np
    
H1_WINS = -1
H2_WINS = 1
TIE = 0


def high_card_winner(vals1, vals2):
    """ high_card_winner()
    parameter
    vals1: list of values from player 1's hand
    vals2: list of values from player 2's hand

    return
    1: Player 1 wins
    0: Tie
    -1: player 2 wins
    """
    vals1 = sorted(vals1, reverse=True)
    vals2 = sorted(vals2, reverse=True)
    while(len(vals1)>0 and len(vals2)>0):
        if (vals1[0] != vals2[0]):
            return H1_WINS if vals1[0] > vals2[0] else H2_WINS 
        vals1 = vals1[1:]
        vals2 = vals2[1:]

    return TIE


def comp_hands(hand1, hand2):
    """ comp_hands(hand1, hand2)
    parameters
    hand1: 5 cards given to one player
    hand2: 5 cards given to another player
    
    returns
    (H1_WINS/H2_WINS/TIE, winning type, losing type)
    """
    h1v, h1s = zip(*hand1)
    h1vals = [simulation.VALUE_VALUES[x] for x in h1v]
    h2v, h2s = zip(*hand2)
    h2vals = [simulation.VALUE_VALUES[x] for x in h2v]
    type1 = simulation.get_hand_rank(hand1) 
    type2 = simulation.get_hand_rank(hand2) 
   
    # If both hands are the same type, figure out which one is the
    # winner. Some can be found based on the highest card, but others
    # need to look at which cards are in play.
    if (type1 == type2):
        if (type1 == simulation.ROYAL_FLUSH):
            return (TIE, simulation.ROYAL_FLUSH, simulation.ROYAL_FLUSH)
        elif (type1 == simulation.FOUR_KIND):
            # Compare the 4 of a kind values
            h1_4 = h1vals[0] if h1vals[0] in h1vals[1:] else h1vals[1]
            h2_4 = h2vals[0] if h2vals[0] in h2vals[1:] else h2vals[1]
#            print('quadruples',h1_4,'vs',h2_4)
            # Cannot tie in a 4-kind
            if (h1_4 > h2_4): return (H1_WINS, simulation.FOUR_KIND, simulation.FOUR_KIND)
            else: return (H2_WINS, simulation.FOUR_KIND, simulation.FOUR_KIND)

        elif (type1 == simulation.FULL_HOUSE):
            # Compare the 3 of a kind. Since only 1 deck is used, we don't need to check the pair too
            h1_v = list(set(h1vals))
            h2_v = list(set(h2vals))
            h1_3 = h1_v[0] if h1vals.count(h1_v[0]) == 3 else h1_v[1]
            h2_3 = h2_v[0] if h1vals.count(h1_v[0]) == 3 else h1_v[1]
#            print('Triples: ', h1_3,'vs',h2_3)
            if (h1_3 > h2_3): return (H1_WINS, simulation.FULL_HOUSE, simulation.FULL_HOUSE)
            else: return (H2_WINS, simulation.FULL_HOUSE, simulation.FULL_HOUSE)
            
        elif (type1 == simulation.THREE_KIND):
            h1_v = list(set(h1vals))
            h2_v = list(set(h2vals))
            if (h1vals.count(h1_v[0]) == 3):
                h1_3 = h1_v[0]
            elif (h1vals.count(h1_v[1]) == 3):
                h1_3 = h1_v[1]
            else:
                h1_3 = h1_v[2]

            if (h2vals.count(h2_v[0]) == 3):
                h2_3 = h2_v[0]
            elif (h1vals.count(h2_v[1]) == 3):
                h2_3 = h2_v[1]
            else:
                h2_3 = h2_v[2]

#            print('Triples: ', h1_3, 'vs', h2_3)

            if (h1_3 > h2_3): return (H1_WINS, simulation.THREE_KIND, simulation.THREE_KIND)
            else: return (H2_WINS, simulation.THREE_KIND, simulation.THREE_KIND)

        elif (type1 == simulation.TWO_PAIR):
            h1_v = sorted(list(set(h1vals)))
            h2_v = sorted(list(set(h2vals)))
            # Find the two pairs for each hand (p1 > p2)
            if (h1vals.count(h1_v[0]) == 1):
                h1p1 = h1_v[1]
                h1p2 = h1_v[2]
            elif (h1vals.count(h1_v[1]) == 1):
                h1p1 = h1_v[0]
                h1p2 = h1_v[2]
            else:
                h1p1 = h1_v[0]
                h1p2 = h1_v[1]

            if (h2vals.count(h2_v[0]) == 1):
                h2p1 = h2_v[1]
                h2p2 = h2_v[2]
            elif (h2vals.count(h2_v[1]) == 1):
                h2p1 = h2_v[0]
                h2p2 = h2_v[2]
            else:
                h2p1 = h2_v[0]
                h2p2 = h2_v[1]

#            print('High pairs: ', h1p1, 'vs',h2p1)
#            print('Low pairs: ', h1p2, 'vs',h2p2)

            if (h1p1 > h2p1):
                return (H1_WINS, simulation.TWO_PAIR, simulation.TWO_PAIR)
            elif (h2p1 > h1p1):
                return (H2_WINS, simulation.TWO_PAIR, simulation.TWO_PAIR)
            elif (h1p2 > h2p2):
                return (H1_WINS, simulation.TWO_PAIR, simulation.TWO_PAIR)
            elif (h2p2 > h1p2):
                return (H2_WINS, simulation.TWO_PAIR, simulation.TWO_PAIR)
            else: return (high_card_winner(h1vals, h2vals), simulation.TWO_PAIR, simulation.TWO_PAIR)
            

        elif (type1 == simulation.PAIR):
            # Find the pair, if the pairs are the same, high card wins
            h1_v = list(set(h1vals))
            h2_v = list(set(h2vals))
#            print(h1vals)
#            print(h2vals)
#            print(h1_v)
#            print(h2_v)
            h1p = list(filter(lambda x: h1vals.count(x) == 2,h1_v))
            h2p = list(filter(lambda x: h2vals.count(x) == 2,h2_v))
#            print('Pairs (p1 vs p2)',h1p,'vs',h2p)
            h1p = h1p[0]
            h2p = h2p[0]
            if (h1p > h2p):
                return (H1_WINS, type1, type1)
            elif (h2p > h1p):
                return (H2_WINS, type1, type1)
            else:
                return (high_card_winner(h1vals, h2vals), type1, type1)
            
        else:
            return (high_card_winner(h1vals, h2vals), type1, type2)
    # If they are different hand-ranks, find the winner
    return (H1_WINS, type1, type2) if (type1 < type2) else (H2_WINS,type2, type1)

def simulate(rounds):
    """simulate(players, rounds)
    This function simulats rounds rounds of a deal of poker to two
    players. It will keep track of how many times a certain hand 
    beats each other hand.
    parameters:
    rounds: number of deals to simulate 
    """
    p1wins=0
    p2wins=0
    ties=0
    handTypeWins=np.zeros((11,11))

    d = simulation.shuffled_deck()

    for i in range(rounds):
        simulation.shuffle(d)
        h1, h2 = simulation.deal_n_cards_to_h_hands(d,5,2)
#        print(h1, ' vs ', h2)
        (winner, winType, loseType) = comp_hands(h1, h2)
#        print(winner, 'won', winType, ' >= ', loseType)
        if (winner == H1_WINS): p1wins+=1
        elif (winner == H2_WINS): p2wins+=1
        else: ties+=1
        handTypeWins[winType][loseType]+=1
    
    print('iterations:%s%d:'%(simulation.DELIM,rounds))
    print("Number of times each hand beat each other")
    print(',',end='')
    for i in range(1,11):
        print(simulation.HAND_RANKS[i], end=simulation.DELIM)
    print()
    for i in range(1,11):
        print(simulation.HAND_RANKS[i], end=simulation.DELIM)
        for j in range(1,11):
             print(handTypeWins[i][j], end=simulation.DELIM)
        print()

    print('Player 1 won %s%d'%(simulation.DELIM,p1wins))
    print('Player 2 won %s%d'%(simulation.DELIM,p2wins))
    print('Players tied %s%d'%(simulation.DELIM,ties))

if __name__=='__main__':
    simulate(10000000)
