
def read_money_from_file():
    try:
        with open("money.txt", 'r') as file:
            money = float(file.read())
    except FileNotFoundError:
        print("File not found")
    return money


def write_money_to_file(money):
    try:
        with open("money.txt", 'w') as file:
            file.write(str(money))
    except FileNotFoundError:
        print("File not found")