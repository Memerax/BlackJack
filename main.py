import random


def main():
    deck = create_deck()
    shuffle_deck(deck)
    player_hand(deck)


def create_deck():
    # Could have just created them all by hand, but I try to stick
    # to the do not repeat yourself concept where possible
    cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
             "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    deck = []
    for card in cards:
        for suit in suits:
            if card.isdigit():
                deck.append([card, suit, int(card)])
            elif card == "Ace":
                deck.append([card, suit, 1, 11])
            else:
                deck.append([card, suit, 10])
    return deck


def player_hand(deck):
    cards = [draw_card(deck), draw_card(deck)]
    points = cards[0][2] + cards[1][2]
    while points < 22:
        print_cards(cards)
        hit_or_stand = input("\nhit/stand: ")
        if hit_or_stand.lower() == "stand":
            return points
        elif hit_or_stand.lower() == "hit":
            card = draw_card(deck)
            cards.append(card)
            if card[0] == 'Ace' and points < 11:
                while True:
                    try:
                        one_or_eleven = int(input("Do you want the ace to be 1? or 11 (1/11):"))
                        if one_or_eleven == 1 or one_or_eleven == 11:
                            points += one_or_eleven
                    except ValueError:
                        print("Not a valid input")
            else:
                points += card[2]
        else:
            print("invalid input")
    print("Bust")
    return points


def print_cards(cards):
    for i in cards:
        print(f"{i[0]} of {i[1]}")


def draw_card(deck):
    card = deck.pop(0)
    return card


def shuffle_deck(deck):
    random.shuffle(deck)


if __name__ == '__main__':
    main()
