import random
import time


def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")
    while True:
        # create Deck
        deck = create_deck()
        # shuffle deck
        shuffle_deck(deck)
        # get bet data
        bet_data()
        # get dealers hole cards
        dealers_hole_cards = [draw_card(deck), draw_card(deck)]
        # Deal player cards and get points
        player_points = player_hand(deck)
        # play the dealers hand
        dealer_points = dealer_hand(deck, dealers_hole_cards)
        # determine the winner
        determine_winner(player_points, dealer_points)
        input("Play again? (y/n): ")


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
                deck.append([card, suit, 1])
            else:
                deck.append([card, suit, 10])
    return deck


def player_hand(deck):
    cards = [draw_card(deck), draw_card(deck)]
    points = cards[0][2] + cards[1][2]
    print_cards(cards, "player")
    while points < 22:
        hit_or_stand = input("\nhit/stand: ")
        if hit_or_stand.lower() == "stand":
            return points
        elif hit_or_stand.lower() == "hit":
            card = draw_card(deck)
            cards.append(card)
            print_cards(cards, "player")
            if card[0] == 'Ace' and points < 11:
                points += is_ace()
            else:
                points += card[2]
        else:
            print("invalid input")
    print("\nBust\n")
    return points


def dealer_hand(deck, dealt):
    cards = dealt
    points = cards[0][2] + cards[1][2]
    print_cards(cards, "Dealer")
    while points < 18:
        time.sleep(1)
        card = draw_card(deck)
        cards.append(card)
        print(f"{card[0]} of {card[1]}")
        if card[0] == 'Ace' and points < 11:
            points += 11
        else:
            points += card[2]
        if points > 21:
            print("Dealer busts")
            return points
    print(f"Dealer has {points} points")
    return points


def is_ace():
    while True:
        try:
            one_or_eleven = int(input("Do you want the ace to be 1? or 11 (1/11):"))
            if one_or_eleven == 1 or one_or_eleven == 11:
                return one_or_eleven
            else:
                print("not a valid number")
        except ValueError:
            print("Not a valid input")


def print_cards(cards, player):
    if player == "player":
        print("\nYOUR CARDS:")
    else:
        print("\nDEALERS CARDS")
    for i in cards:
        print(f"{i[0]} of {i[1]}")


def draw_card(deck):
    card = deck.pop(0)
    return card


def shuffle_deck(deck):
    random.shuffle(deck)


def bet_data():
    with open("money.txt") as file:
        money = file.read()
    print(f"Money: {money}")
    bet = input("Bet amount: ")


def determine_winner(player_points, dealer_points):
    print(f"\nYOUR POINTS:  {player_points}")
    print(f"DEALERS POINTS   {dealer_points}\n")
    if player_points > dealer_points:
        print("Congrats you win.")
    else:
        print("Sorry. You lose.")


if __name__ == '__main__':
    main()
