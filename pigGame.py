import random


def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)


# Input validation for number of players
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

# Game loop
while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "'s turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        # Rolling phase
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score this turn is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score now is:", player_scores[player_idx])

        # Check if the player has reached the max score after this turn
        if player_scores[player_idx] >= max_score:
            break  # Exit the loop if we have a winner

    # Show current standings after each round
    print("\nCurrent scores:")
    for idx, score in enumerate(player_scores):
        print(f"Player {idx + 1}: {score}")

# Determine the winner(s)
max_score = max(player_scores)
winners = [idx + 1 for idx, score in enumerate(player_scores) if score == max_score]

if len(winners) > 1:
    print("It's a tie! Players", " and ".join(map(str, winners)), "are the winners with a score of:", max_score)
else:
    print("Player number", winners[0], "is the winner with a score of:", max_score)
