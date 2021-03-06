import enum
import random


class Suit(enum.Enum):
    Clubs = enum.auto()
    Hearts = enum.auto()
    Spades = enum.auto()
    Diamonds = enum.auto()


class Rank(enum.Enum):
    Ace = enum.auto()
    Two = enum.auto()
    Three = enum.auto()
    Four = enum.auto()
    Five = enum.auto()
    Six = enum.auto()
    Seven = enum.auto()
    Eight = enum.auto()
    Nine = enum.auto()
    Ten = enum.auto()
    Jack = enum.auto()
    Queen = enum.auto()
    King = enum.auto()


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        # return "<Card(" + self.rank.name + ", " + self.suit.name + ")>"
        # return "<Card({0}, {1})>".format(self.rank.name, self.suit.name)
        return f"<Card({self.rank.name}, {self.suit.name})>"


def make_deck():
    deck = []
    for suit in Suit:
        for rank in Rank:
            card = Card(rank, suit)
            deck.append(card)
    return deck


def deal(d):
    """Removes and returns first card of the deck."""
    return d.pop(0)


def card_point(x):
    n = x.rank
    if n == Rank.Ace:
        return 11
    if n == Rank.Two:
        return 2
    if n == Rank.Three:
        return 3
    if n == Rank.Four:
        return 4
    if n == Rank.Five:
        return 5
    if n == Rank.Six:
        return 6
    if n == Rank.Seven:
        return 7
    if n == Rank.Eight:
        return 8
    if n == Rank.Nine:
        return 9
    if n == Rank.Ten:
        return 10
    if n == Rank.Jack:
        return 10
    if n == Rank.Queen:
        return 10
    if n == Rank.King:
        return 10


def main():
    deck = make_deck()
    random.shuffle(deck)
    hand = []

    the_house = []
    dealer_card = deal(deck)
    dealer_card2 = deal(deck)
    the_house.append(dealer_card)
    the_house.append(dealer_card2)
    house_total = card_point(dealer_card)
    house_total += card_point(dealer_card2)

    # add_to_hand(dealt_card)
    dealt_card = deal(deck)
    dealt_card2 = deal(deck)
    hand.append(dealt_card)
    hand.append(dealt_card2)
    total = card_point(dealt_card)
    total += card_point(dealt_card2)

    # "Play Loop"
    play = True
    while play:

        # Evaluates point for both players to determine a winner and a loop break condition. If a break condition is
        # not met, continue to beginning of "Play Loop".
        if total == 21 and house_total == 21:
            print(f'The House: {house_total, the_house}')
            print(f'Player 1: {total, hand}: \n WHOA DOUBLE BLACKJACK!')
            break
        if total == 21 and house_total != 21:
            print(f'The House: {house_total, the_house}')
            print(f'BLACKJACK! {total, hand}: \nYOU WIN!')
            break
        if house_total == 21 and total != 21:
            print(f'Player 1: {total, hand}')
            print(f'BLACKJACK! {house_total, the_house}: \nHouse wins!')
            break
        if house_total < 21 < total:
            print(f'The House: {house_total, the_house}')
            print(f'You Bust! {total, hand}: \nHouse Wins!')
            break
        if house_total > 21 > total:
            print(f'Player 1: {total, hand}')
            print(f'House Busts:{house_total, the_house}: \nYou Win!')
            break
        if total > 21 and house_total > 21:
            print(f'Player has {total, hand} \nThe House has {house_total, the_house} \nboth players Bust!')
            if __name__ == "__main__":
                main()
        print("")

        print(f'Player 1: {hand}')
        print(f'The House: {the_house}')

        print("")

        # get_hos is "Hit or Stay".
        get_hos = input(f'Your Total is {total} and The House has {house_total}, would you like to Hit? ("y" or "n"): ')

        print("")

        # if get_hos is 'y' both player 1 and The House take cards. If 'n' then only The House takes a card. #Beta
        # Version haha
        if get_hos == 'y':
            d = deal(deck)
            hd = deal(deck)

            hand.append(d)
            the_house.append(hd)

            total += card_point(d)
            house_total += card_point(hd)

        if get_hos == 'n':
            continue
        else:
            continue

    # "Leaving Loop": Ask players if they want to play again or not. I am using 'else' instead of "try/except" to get
    # around value errors.
    leaving = True
    while leaving:
        print("")
        play_again = input("Would you like to play again? ('y' or 'n'): ")
        if play_again == 'y':
            leaving = False
            if __name__ == "__main__":
                main()
        if play_again == 'n':
            print('Goodbye!')
            exit()
        else:
            print('Please Choose "y" or "n"!')
            continue


if __name__ == "__main__":
    main()
