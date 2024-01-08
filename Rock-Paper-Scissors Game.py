import random

def rock_paper_scissors():
    # Score tracking
    user_score = 0
    computer_score = 0

    while True:
        # User input
        user_choice = input("Choose rock, paper, or scissors: ")

        # Computer selection
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer_choice}")

        # Game logic
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

        # Display result
        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")

        # Play again
        play_again = input("Do you want to play another round? (yes/no): ")
        if play_again.lower() != "yes":
            break

# Run the game
rock_paper_scissors()
