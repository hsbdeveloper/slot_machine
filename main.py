import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    ":D" : 2,
    ":)" : 4,
    ":O" : 6,
    ":(" : 8
}

symbol_value = {
    ":D" : 5,
    ":)" : 4,
    ":O" : 3,
    ":(" : 2
}

def check_winnings(columns, lines, bet, values):
    win_amount = 0
    win_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            win_amount += values[symbol] * bet
            win_lines.append(lines + 1)
    
    return win_amount, win_lines


def slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():    
        for _ in range(symbol_count):
            all_symbols.append(symbol)   
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else: 
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number!")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Please enter a number!")
    return lines    

def get_bet():
    while True:
        amount = input("What would you like to bet? £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.")
        else:
            print("Please enter a number")
    return amount

def per_spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is £{balance}")
        else:
            break
    print(f"You are betting £{bet} on {lines} lines. Total bet is equal to: £{total_bet}.")

    slots = slot_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    win_amount, win_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won £{win_amount}")
    print(f"You won on lines:", *win_lines)
    return win_amount - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is £{balance}")
        answer = input("Press enter to spin or q to quit")
        if answer == "q":
            break
        balance += per_spin(balance)
    print(f"You left with £{balance}")
    
main()