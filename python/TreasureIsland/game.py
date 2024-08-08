import location
import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 3
    print("\nWelcome to the Guess the Number game!")
    print("I have chosen a number between 1 and 10. You have 3 attempts to guess it.\n")
    
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        if guess == number_to_guess:
            print("\nCongratulations! You guessed the correct number!\n")
            return True
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")
        
        attempts -= 1
        if attempts > 0:
            print(f"Try again. You have {attempts} attempts left.\n")
    
    print(f"Sorry, you're out of attempts. The correct number was {number_to_guess}.\n")
    return False

def riddle_game():
    print("\nWelcome to the Riddle game!")
    print("You have to answer 3 questions, and at least 2 must be correct to move forward.")
    
    correct_answers = 0
    
    # Question 1
    print("1. You measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy.")
    answer = input("Enter your answer: ").lower().strip()
    if answer == "a candle":
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect. The correct answer is 'a candle'.")
    
    # Question 2
    print("2. I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?")
    answer = input("Enter your answer: ").lower().strip()
    if answer == "a map":
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect. The correct answer is 'a map'.")
    
    # Question 3
    print("3. What goes up but never comes down?")
    answer = input("Enter your answer: ").lower().strip()
    if answer == "your age":
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect. The correct answer is 'your age'.")
    
    print(f"\nYou answered {correct_answers} out of 3 questions correctly.")
    if correct_answers >= 2:
        print("Congratulations! You can move forward.")
        return True
    else:
        print("You didn't answer enough questions correctly. Try again next time.")
        return False

def pattern_game():
    print("\nSolve the pattern: 3, 6, 11, 18, __")
    print("Hint: The pattern increases by consecutive prime numbers (3, 5, 7, 11, ...)")
    answer = input("Enter the next number in the pattern: ").strip()
    if answer == "29":
        print("Congratulations! You solved the pattern!")
        return True
    else:
        print("Incorrect. The correct answer is 29.")
        return False

def treasure_chamber_doors():
    print("\nYou are in the treasure chamber. There are three doors in front of you:")
    print("A) Door A")
    print("B) Door B")
    print("C) Door C")
    
    choice = input("Which door do you choose? (A/B/C): ").lower().strip()
    
    if choice == 'a':
        print("\nYou chose Door A... and were eaten by a monster! Game over.\n")
        return False
    
    elif choice == 'b':
        print("\nYou chose Door B. You must solve a pattern to proceed.\n")
        if pattern_game():
            print("\nYou solved the pattern, but you got lost and ended up back where you started.\n")
            return False
        else:
            return False
    
    elif choice == 'c':
        print("\nYou chose Door C. Congratulations! You found the hidden treasure without any further challenges!\n")
        return True
    
    else:
        print("Invalid choice. Try again.")
        return treasure_chamber_doors()

def process_input(player_input, curr_loc):
    actions = location.island_map[curr_loc]["actions"]
    if player_input in actions:
        new_location = actions[player_input]
        if new_location == "jungle":
            if guess_the_number():
                return new_location 
            else:
                return curr_loc
        elif new_location == "cave":
            if riddle_game():
                return new_location 
            else:
                return curr_loc  
        elif new_location == "treasure chamber":
            if treasure_chamber_doors():
                treasures = ['gem', 'ruby', 'diamond', 'coin', 'emerald', 'goblet']
                print(f"You found the following treasures: {', '.join(treasures)}")
                return new_location
            else:
                return curr_loc
        return new_location
    elif player_input == "quit":
        return "quit"
    else:
        print("Invalid action. Try again.\n")
        return curr_loc

curr_loc = location.current_location

while True:
    location.show_curr(curr_loc)
    player_input = input("\nWhat do you want to do? ").lower()
    curr_loc = process_input(player_input, curr_loc)

    if curr_loc == "treasure chamber":
        print("\nCongratulations! You have found the hidden treasure!\n")
        break
    
    if curr_loc == "quit":
        print("\nThank you for playing! Goodbye.\n")
        break
