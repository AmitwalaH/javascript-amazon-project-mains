import random

def welcome_message():
    print("\nWelcome to the Treasure Island Adventure Game!")
    print("Discover a legendary treasure hidden on this mysterious island.")
    print("Explore, solve puzzles, and overcome challenges to find the treasure.")
    print("Type 'quit' at any time to end your adventure.\n")

def show_current_location(location):
    if location == "beach":
        print("You are on a sunny beach. A jungle is ahead.")
        print("Possible actions: go north")
    elif location == "jungle":
        print("You are in a dense jungle. A cave is to the east and ancient ruins are to the west.")
        print("Possible actions: go south, go east, go west")
    elif location == "cave":
        print("You are in a dark cave. There is a passage deeper in.")
        print("Possible actions: go west, go deeper")
    elif location == "ruins":
        print("You are among ancient ruins. There is a path back to the jungle.")
        print("Possible actions: go east")
    elif location == "treasure_chamber":
        print("You have found the treasure chamber! Congratulations!")
        print("Possible actions: go back")

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 3
    print("\nGuess a number between 1 and 10. You have 3 attempts.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == number_to_guess:
            print("Correct!")
            return True
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left.")
    print(f"Sorry, the correct number was {number_to_guess}.")
    return False

def riddle_game():
    print("\nAnswer at least 2 out of 3 riddles correctly to proceed.")
    correct_answers = 0

    # Riddle 1
    print("1. I have cities, but no houses; mountains, but no trees; water, but no fish. What am I?")
    print("A. A map  B. A dream  C. A desert")
    answer = input("Enter your answer (A, B, or C): ").upper()
    if answer == "A":
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect. The answer is A: A map.")

    # Riddle 2
    print("2. I have space, but no room. You can enter, but can't go inside. What am I?")
    print("A. A box  B. A library  C. A mailbox")
    answer = input("Enter your answer (A, B, or C): ").upper()
    if answer == "C":
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect. The answer is C: A mailbox.")

    # Riddle 3
    print("3. What can run but never walks, has a mouth but never talks, has a bed but never sleeps?")
    print("A. A river  B. A book  C. A wind")
    answer = input("Enter your answer (A, B, or C): ").upper()
    if answer == "A":
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect. The answer is A: A river.")

    print(f"\nYou answered {correct_answers} out of 3 riddles correctly.")
    if correct_answers >= 2:
        print("You solved the riddles.")
        return True
    else:
        print("Not enough correct answers. Try again later.")
        return False

def pattern_game():
    print("\nSolve the pattern: 1, 4, 9, 16, ...")
    answer = int(input("What is the next number? "))
    if answer == 25:
        print("Correct!")
        return True
    else:
        print("Incorrect. The correct answer is 25.")
        return False

def treasure_chamber_doors():
    print("\nChoose one of three doors:")
    print("A. The Ornate Door")
    print("B. The Mysterious Door")
    print("C. The Simple Door")

    choice = input("Choose a door (A, B, or C): ").upper()

    if choice == 'A':
        print("Behind the Ornate Door lies a fierce guardian. Game Over!")
        return "game_over"

    elif choice == 'B':
        print("The Mysterious Door requires you to solve a riddle.")
        if riddle_game():
            print("You solved the riddle! The door opens.")
            return True
        else:
            return False

    elif choice == 'C':
        print("The Simple Door presents a number sequence challenge.")
        if pattern_game():
            print("You solved the pattern! The door opens.")
            return True
        else:
            return False

    else:
        print("Invalid choice. Please choose A, B, or C.")
        return treasure_chamber_doors()

def process_input(player_input, current_location):
    if current_location == "beach":
        if player_input == "go north":
            if guess_the_number():
                return "jungle"
            else:
                return "beach"
        else:
            print("Invalid action. Try again.")
            return current_location

    elif current_location == "jungle":
        if player_input == "go south":
            return "beach"
        elif player_input == "go east":
            if riddle_game():
                return "cave"
            else:
                return "jungle"
        elif player_input == "go west":
            return "ruins"
        else:
            print("Invalid action. Try again.")
            return current_location

    elif current_location == "cave":
        if player_input == "go west":
            return "jungle"
        elif player_input == "go deeper":
            result = treasure_chamber_doors()
            if result == True:
                return "treasure_chamber"
            elif result == "game_over":
                return "game_over"
            else:
                return current_location
        else:
            print("Invalid action. Try again.")
            return current_location

    elif current_location == "ruins":
        if player_input == "go east":
            return "jungle"
        else:
            print("Invalid action. Try again.")
            return current_location

    elif current_location == "treasure_chamber":
        if player_input == "go back":
            return "cave"
        else:
            print("Invalid action. Try again.")
            return current_location

    elif player_input == "quit":
        return "quit"
    
    else:
        print("Invalid action. Try again.")
        return current_location

welcome_message()
current_location = "beach"

while True:
    show_current_location(current_location)
    player_input = input("What do you want to do? ").lower()
    current_location = process_input(player_input, current_location)

    if current_location == "treasure_chamber":
        print("Congratulations! You've found the legendary treasure!")
        break

    if current_location == "game_over":
        print("Game Over!")
        break

    if current_location == "quit":
        print("Thanks for playing!")
        break
