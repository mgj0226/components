import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_cnt = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_cnt in symbols.items():
        for _ in range(symbol_cnt):
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
        amt = input("Deposit: $")
        if amt.isdigit():
            amt =int(amt)
            if amt > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amt

def get_number_of_lines():
    while True:
        lines = input("Number of lines to bet on (1-" + str(MAX_LINES)+"): ")
        if lines.isdigit():
            lines =int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print(f"Enter only(1 - {MAX_LINES}).")
        else:
            print("Please enter a number.")
    return lines
def get_bet():
    while True:
        amt = input("Bet on each line: $")
        if amt.isdigit():
            amt =int(amt)
            if MIN_BET<= amt <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}." )
        else:
            print("Please enter a number.")
    return amt

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not enough money to bet. Current balance is {balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_cnt)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    
    while True:
        print(f"Current balance is ${balance}")
        if balance == 0:
            print("Game Over")
            break
        ans = input("Press enter to spin (q to quit).")
        if ans == "q":
            break        
        balance += spin(balance)

    print(f"You left with ${balance}")
main()