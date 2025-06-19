import random
import string

class User:
    def __init__(self, user_id, name, password):
        self.details = (user_id, name, password)

    def display(self):
        print(f"User ID: {self.details[0]}")
        print(f"Name: {self.details[1]}")
        print(f"Password: {self.details[2]}")

def generate_password(user_input_words):
    try:
        if not user_input_words or len(user_input_words) < 3:
            raise ValueError("Please enter at least 3 words to generate a strong password.")

        # Choose random words
        selected_words = random.sample(user_input_words, 2)
        print(selected_words)

        # Add random capital letters
        capital_letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        print(capital_letters)
        
        # Add random digits
        numbers = ''.join(random.choices(string.digits, k=2))
        print(numbers)
        
        # Add random special characters
        special_chars = ''.join(random.choices('!@#$%^&*()-_=+[]{};:', k=2))
        print(special_chars)
        
        # Combine all parts and shuffle
        raw_password = ''.join(selected_words) + capital_letters + numbers + special_chars
        password_list = list(raw_password)
        random.shuffle(password_list)

        final_password = ''.join(password_list)

        # Ensure length is at least 8
        if len(final_password) < 8:
            final_password += ''.join(random.choices(string.ascii_letters + string.digits, k=8 - len(final_password)))

        return final_password
    except Exception as e:
        print("Error:", e)
        return None

# Main program
try:
    user_id = input("Enter user ID: ")
    name = input("Enter your name: ")
    words_input = input("Enter a few words separated by spaces (e.g. hobby, pet, favorite food): ")

    user_words = words_input.strip().split()
    print(type(user_words))
    print(user_words)

    password = generate_password(user_words)

    if password:
        user = User(user_id, name, password)
        print("\n✅ User account created successfully!")
        user.display()
    else:
        print("Failed to create password.")

except Exception as e:
    print("Unexpected error:", e)
