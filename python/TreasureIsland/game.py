import location
import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 3
    print("\nWelcome to the Guess the Number game!")
    print("I have chosen a number between 1 and 10. You have 3 attempts to guess it.\n")
    
    while attempts > 0:
        try:
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
        except ValueError:
            print("Please enter a valid number.\n")
    
    print(f"Sorry, you're out of attempts. The correct number was {number_to_guess}.\n")
    return False

def riddle_game():
    print("\nWelcome to the Riddle game!")
    print("\nYou have to answer 3 questions, and at least 2 must be correct to move forward.")
    
    correct_answers = 0
    
    # Question 1
    q1 = "1. You measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy."
    ans_of_q1 = "a candle"
    print(q1)
    u_in = input("Enter your answer: ").lower().strip()
    if ans_of_q1 == u_in:
        print("Hurry! You are correct!")
        correct_answers += 1
    else:
        print("Sorry, that's incorrect. The answer is 'a candle'.")
    
    # Question 2
    q2 = "2. I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?"
    ans_of_q2 = "a map"
    print(q2)
    u_in = input("Enter your answer: ").lower().strip()
    if ans_of_q2 == u_in:
        print("Hurry! You are correct!")
        correct_answers += 1
    else:
        print("Sorry, that's incorrect. The answer is 'a map'.")
    
    # Question 3
    q3 = "3. What goes up but never comes down?"
    ans_of_q3 = "your age"
    print(q3)
    u_in = input("Enter your answer: ").lower().strip()
    if ans_of_q3 == u_in:
        print("Hurry! You are correct!")
        correct_answers += 1
    else:
        print("Sorry, that's incorrect. The answer is 'your age'.")
    
    print(f"\nYou answered {correct_answers} out of 3 questions correctly.")
    if correct_answers >= 2:
        print("Congratulations! You have answered enough questions correctly to move forward.")
        return True
    else:
        print("Unfortunately, you didn't answer enough questions correctly. Try again next time.")
        return False

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