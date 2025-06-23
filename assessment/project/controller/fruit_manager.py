import json
from datetime import datetime
import os

STOCK_FILE = 'fruit_stock.json'
LOG_FILE = 'transaction_log.txt'

# Load stock data from file
def load_stock():
    if not os.path.exists(STOCK_FILE):
        return {}
    with open(STOCK_FILE, 'r') as file:
        return json.load(file)

# Save stock data to file
def save_stock(stock):
    with open(STOCK_FILE, 'w') as file:
        json.dump(stock, file, indent=4)

# Log transactions
def log_transaction(message):
    with open(LOG_FILE, 'a') as log:
        log.write(f"[{datetime.now()}] {message}\n")

def add_fruit():
    stock = load_stock()
    fruit = input("Enter fruit name: ").capitalize()
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    if fruit in stock:
        stock[fruit]['quantity'] += qty
        stock[fruit]['price'] = price
    else:
        stock[fruit] = {'quantity': qty, 'price': price}

    save_stock(stock)
    log_transaction(f"Added {qty} {fruit}(s) at price {price}.")
    print("Fruit added successfully.")

def view_fruit():
    stock = load_stock()
    if not stock:
        print("No fruits in stock.")
    else:
        print("\n--- Available Fruit Stock ---")
        for fruit, info in stock.items():
            print(f"{fruit}: Quantity = {info['quantity']}, Price = {info['price']}")
        print("-----------------------------")

def update_fruit():
    stock = load_stock()
    fruit = input("Enter fruit name to update: ").capitalize()

    if fruit in stock:
        qty = int(input("Enter new quantity: "))
        price = float(input("Enter new price per unit: "))
        stock[fruit]['quantity'] = qty
        stock[fruit]['price'] = price
        save_stock(stock)
        log_transaction(f"Updated {fruit}: Quantity = {qty}, Price = {price}")
        print("Fruit updated successfully.")
    else:
        print("Fruit not found in stock.")
