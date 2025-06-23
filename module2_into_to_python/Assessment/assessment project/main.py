import sys
from controller import fruit_manager, customer

def display_menu():
    print("\n=== Fruit Store Console Application ===")
    print("1. Add Fruit Stock")
    print("2. View Fruit Stock")
    print("3. Update Fruit Stock")
    print("4. Buy Fruit")
    print("5. Exit")

while True:
    try:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            fruit_manager.add_fruit()
        elif choice == '2':
            fruit_manager.view_fruit()
        elif choice == '3':
            fruit_manager.update_fruit()
        elif choice == '4':
            customer.buy_fruit()
        elif choice == '5':
            print("Exiting the application. Thank you!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
