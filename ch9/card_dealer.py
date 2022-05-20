# this porgram uses a distinary as a desk of cards


def main():
    deck = create_deck()

    num_cards = int(input('How many cards should I deal? '))

    deal_cards(deck, num_cards)


def create_deck():
    deck = {'Ace of spades': 1, '2 of spades': 2, '3 of spades': 3,
            '4 of spades': 4, '5 of spades': 5, '6 of spades': 6,
            '7 of spades': 7, '8 of spades': 8, '9 of spades': 9,
            '10 of spades': 10, 'Jack of spades': 10,
            'Queen of spades': 10, 'king of spades': 10,

            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
            '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of Clubs': 1, '2 of clubs': 2, '3 of clubs': 3,
            '4 of clubs': 4, '5 of clubs': 5, '6 of clubs': 6,
            '7 of clubs': 7, '8 of clubs': 8, '9 of clubs': 9,
            '10 of clubs': 10, 'Jack of clubs': 10,
            'Queen of clubs': 10, 'King of clubs': 10,

            'Ace of diamond': 1, '2 of diamonds': 2, '3 of diamonds': 3,
            '4 of diamonds': 4, '5 of diamonds': 5, '6 of diamonds': 6,
            '7 of diamonds': 7, '8 of diamonds': 8, '9 of diamonds': 9,
            '10 of diamonds': 10, 'jack of diamonds': 10,
            'Queen of diamonds': 10, 'king of diamonds': 10
            }

    return deck
