import random
from art import logo
from art import vs
from game_data import data
from replit import clear


def format_data(account):
    """Takes the account data and returns the the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
score = 0

# Make the game repeatable
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    print(logo)

    # Generate a random account from the game delattr
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for guess
    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follower account of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_a["follower_count"]
    ## Use if statement to check if the answer is correct

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        clear()
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        clear()
        print(f"Sorry, that's wrong. Final score: {score}")

    # Making the account at position B become the next account at position A.

    # Clear the screen between rounds
