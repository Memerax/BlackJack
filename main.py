import random


def main():
    money = read_money_from_file()
    print(money)
    money = 1000
    write_money_to_file(money)


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


def print_deck(deck):
    for i in deck:
        print(i)


def read_money_from_file():
    try:
        with open("money.txt", 'r') as file:
            money = int(file.read())
    except FileNotFoundError:
        print("File not found")
    return money


def write_money_to_file(money):
    try:
        with open("money.txt", 'w') as file:
            file.write(str(money))
    except FileNotFoundError:
        print("File not found")


def draw_card(deck):
    card = deck.pop(0)
    return card


def shuffle_deck(deck):
    random.shuffle(deck)


if __name__ == '__main__':
    main()
