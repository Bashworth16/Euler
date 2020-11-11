"""
FOR REVIEW
"""

# Uni-Card Key:
#       Spade is A, Heart is B, Diamond is C, Club is D
#       (1 - 9) = Ace through 9.
#       A = Ten, B = Jack, D = Queen, E = King
#       u+1 FO {suite:A:Spade}{rank:1:Ace}

# Uni_suit takes a dealt card from the deck and assigns it a unicode variable according to the suit.
# "U0001FO" is the unicode prefix the last two character represent the Suit and Rank.
# e.g. A in "U0001F0A" represents Spades.
def uni_suit(x):
    s = x.suit
    uni_card = "U0001F0"
    if s == Suit.Spades:
        uni_card = f'{uni_card}A'
        return uni_card
    if s == Suit.Hearts:
        uni_card = f'{uni_card}B'
        return uni_card
    if s == Suit.Diamonds:
        uni_card = f'{uni_card}C'
        return uni_card
    if s == Suit.Clubs:
        uni_card = f'{uni_card}D'
        return uni_card


# Uni_rank takes a dealt card AND the uni-card variable passed from the uni_suit(x) function.
# "U0001FO" is the unicode prefix and the last two character represent the suit and rank.
#  E.G. The Ace of Spades is represented by "U0001F0{suit: A}{rank: 1}" where Spades is A and Ace is 1.
def uni_rank(x, s):
    r = x.rank
    uni_card = s
    if r == Rank.Ace:
        uni_card = f'u"\{uni_card}1"'
        return uni_card
    if r == Rank.Two:
        uni_card = f'u"\{uni_card}2"'
        return uni_card
    if r == Rank.Three:
        uni_card = f'u"\{uni_card}3"'
        return uni_card
    if r == Rank.Four:
        uni_card = f'u"\{uni_card}4"'
        return uni_card
    if r == Rank.Five:
        uni_card = f'u"\{uni_card}5"'
        return uni_card
    if r == Rank.Six:
        uni_card = f'u"\{uni_card}6"'
        return uni_card
    if r == Rank.Seven:
        uni_card = f'u"\{uni_card}7"'
        return uni_card
    if r == Rank.Eight:
        uni_card = f'u"\{uni_card}8"'
        return uni_card
    if r == Rank.Nine:
        uni_card = f'u"\{uni_card}9"'
        return uni_card
    if r == Rank.Ten:
        uni_card = f'u"\{uni_card}A"'
        return uni_card
    if r == Rank.Jack:
        uni_card = f'u"\{uni_card}B"'
        return uni_card
    if r == Rank.Queen:
        uni_card = f'u"\{uni_card}D"'
        return uni_card
    if r == Rank.King:
        uni_card = f'u"\{uni_card}E"'
        return uni_card


dealt_card = deal(deck)

suit = uni_suit(dealt_card)
print(f'suit is {suit}')

rank = uni_rank(dealt_card, suit)
print(rank)

# OUTPUT:   suit is U0001F0C
#           u"\U0001F0C4"
#           (This is the correct unicode structure for '🃄' but it only prints the code to console instead of the emoji)