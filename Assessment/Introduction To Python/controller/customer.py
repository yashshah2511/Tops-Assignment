import json
from datetime import datetime
import os

STOCK_FILE = 'fruit_stock.json'
LOG_FILE = 'transaction_log.txt'

# Load stock data
def load_stock():
    if not os.path.exists(STOCK_FILE):
        return {}
    with open(STOCK_FILE, 'r') as file:
        return json.load(file)

# Save stock data
def save_stock(stock):
    with open(STOCK_FILE, 'w') as file:
        json.dump(stock, file, indent=4)

# Log transaction
def log_transaction(message):
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{datetime.now()}] {message}\n")

def buy_fruit():
    stock = load_stock()
    if not stock:
        print("No fruits available to buy.")
        return

    fruit = input("Enter fruit name to buy: ").capitalize()

    if fruit in stock:
        qty = int(input("Enter quantity to buy: "))
        if qty <= stock[fruit]['quantity']:
            total = qty * stock[fruit]['price']
            stock[fruit]['quantity'] -= qty
            save_stock(stock)
            log_transaction(f"Customer bought {qty} {fruit}(s) for Rs.{total}.")
            print(f"Purchase successful. Total amount: Rs.{total}")
        else:
            print("Not enough stock available.")
    else:
        print("Fruit not found.")
