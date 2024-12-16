import random


def get_user_choice():
    print("Choose one: rock, paper, scissors")
    user_input = input("Your choice: ").lower()
    if user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose again.")
        return get_user_choice()
    return user_input


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


while True:
    play_game()

    '''How to play the game:
1.The game starts by asking the user to select "rock", "paper", or "scissors".
2.The computer randomly selects one of the three choices.
3.The game compares the user’s and computer’s choices and determines the winner.
4.The user can choose to play again or quit.
'''