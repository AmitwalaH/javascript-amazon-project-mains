# print("Welcome to Print leap year!!!")

# number = int(input("Insert the Year "));

# if number % 4 == 0:
#     if number % 100 == 0:
#         if number % 400 == 0:
#             print("Its a Leap Year!")
#         else:
#             print("Its not Leap Year!")
#     else:
#         print("Its a Leap Year!")
# else:
#     print("Its not Leap Year!")

# print("Welcome to Pizza Hut!!!")

# totalBill = 0

# size = input("What size pizza do u want? S, M or L ")

# if size == 'S':
#     totalBill = totalBill + 15
# if size == 'M':
#     totalBill = totalBill + 20
# if size == 'L':
#     totalBill = totalBill + 25

# print(f"Total Bill before adding pepperoni and extra cheese = ${totalBill}")        

# add_pepperoni = input("Do you want to add Peperoni? Y or N ")

# if add_pepperoni == 'Y':
#     totalBill = totalBill + 2    

# extra_cheese = input("Do want to add extra Cheese ? Y or N ")

# if extra_cheese == 'Y':
#     totalBill = totalBill + 1

# print(f"Here is your Total Bill : ${totalBill}") 


# first_name = input("What is your name? ")

# second_name = input("What is their name? ")

# first = first_name.lower()

# second = second_name.lower()

# combined = first + second

# t = combined.count("t");
# r = combined.count("r");
# u = combined.count("u");
# e = combined.count("e");
# true = t+r+u+e
# l = combined.count("l");
# o = combined.count("o");
# v = combined.count("v");
# e = combined.count("e");
# love = l+o+v+e

# s_core = str(true) + str(love)

# score = int(s_core)

# if score < 10 or score > 90:
#     print(f"Your score is {score}, you go together like coke abd mentor.")
# elif score >= 40 and score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}")

# `print("Welcome to Tresure Island.")
# print("Your mission is to find the treasure.")
# cross_road = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" ')

# if cross_road == "right":
#     print("Game Over!")
# else:
#     boat = input("You come to lake. Thers is an island in the middle of the lake. Type 'wait' to wait for boat. Type 'swim' to swim across. ")
#     if boat == "wait":
#         door = input("You arrive at island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
#         if door == "red" or door == "blue":
#             print("You enter a room of beasts. Game Over!")
#         else:
#             print("You Won the game, Hurry!")
#     else: 
#         print("Game Over!")`

# import random

# heads = "Heads"

# tails = "Tails"

# ans = random.randint(1,2)

# if ans > 1:
#     print(tails)
# else:
#     print(heads)

# import random

# all_names = input("Give me everybody's names, seperated by comma ")

# names = all_names.split(",")

# index = random.randint(0,(len(names)-1))

# print(f"{names[index]} is going to buy the meal today!")

# row1 = ["💼","💼","💼"]
# row2 = ["💼","💼","💼"]
# row3 = ["💼","💼","💼"]
# map = [row1,row2,row3]

# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? ")

# pos = position

# index_0 = int(pos[0])
# index_1 = int(pos[1])

# map[index_0 - 1][index_1 - 1] = "👻"

# print(map)


# students_heights = [180,124,165,173,189,169,146]

# total = 0

# for heights in students_heights:
#     total += heights

# avg = total / len(students_heights);

# print(total)
# print(int(avg))

# student_scores = input("Input a list of student scores ")

# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)

# temp = 0

# for great in student_scores:
#     if temp < great:
#         temp = great
# print(f"Greatest score is {great}")


# total_even = 0

# for number in range(2 , 100 , 2):
#     total_even+= number
# print(total_even)

# for n in range (1, 20):
#     if n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#     elif n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(n)

# import random

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O' ,'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print("Welcome to the PyPassword Generator!")
# # nr_letters = int(input("How many letters would you like in your password?\n"))
# # nr_symbols = int(input(f"How many symbols would you like?\n"))
# # nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = " "

# # range_letters = len(letters)
# # range_numbers = len(numbers)
# # range_symbols = len(symbols)

s= "Ant"

print(s[-2])

# for n in range(0,)

# Sonar Treasure Hunt by Al Sweigart
# Used here with permission
# Creative Commons - Attribution - Share Alike - Non-Commercial license

# import random
# import sys
# import math

# def getNewBoard():
#     # Create a new 60x15 board data structure.
#     board = []
#     for x in range(60): # The main list is a list of 60 lists.
#         board.append([])
#         for y in range(15): # Each list in the main list has 15 single-character strings.
#             # Use different characters for the ocean to make it more readable.
#             if random.randint(0, 1) == 0:
#                 board[x].append('~')
#             else:
#                 board[x].append('`')
#     return board

# def drawBoard(board):
#     # Draw the board data structure.
#     tensDigitsLine = '    ' # Initial space for the numbers down the left side of the board
#     for i in range(1, 6):
#         tensDigitsLine += (' ' * 9) + str(i)

#     # Print the numbers across the top of the board.
#     print(tensDigitsLine)
#     print('   ' + ('0123456789' * 6))
#     print()

#     # Print each of the 15 rows.
#     for row in range(15):
#         # Single-digit numbers need to be padded with an extra space.
#         if row < 10:
#             extraSpace = ' '
#         else:
#             extraSpace = ''

#         # Create the string for this row on the board.
#         boardRow = ''
#         for column in range(60):
#             boardRow += board[column][row]

#         print('%s%s %s %s' % (extraSpace, row, boardRow, row))

#     # Print the numbers across the bottom of the board.
#     print()
#     print('   ' + ('0123456789' * 6))
#     print(tensDigitsLine)

# def getRandomChests(numChests):
#     # Create a list of chest data structures (two-item lists of x, y int coordinates).
#     chests = []
#     while len(chests) < numChests:
#         newChest = [random.randint(0, 59), random.randint(0, 14)]
#         if newChest not in chests: # Make sure a chest is not already here.
#             chests.append(newChest)
#     return chests

# def isOnBoard(x, y):
#     # Return True if the coordinates are on the board; otherwise, return False.
#     return x >= 0 and x <= 59 and y >= 0 and y <= 14

# def makeMove(board, chests, x, y):
#     # Change the board data structure with a sonar device character. Remove treasure chests from the chests list as they are found.
#     # Return False if this is an invalid move.
#     # Otherwise, return the string of the result of this move.
#     smallestDistance = 100 # Any chest will be closer than 100.
#     for cx, cy in chests:
#         distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

#         if distance < smallestDistance: # We want the closest treasure chest.
#             smallestDistance = distance

#     smallestDistance = round(smallestDistance)

#     if smallestDistance == 0:
#         # xy is directly on a treasure chest!
#         chests.remove([x, y])
#         return 'You have found a sunken treasure chest!'
#     else:
#         if smallestDistance < 10:
#             board[x][y] = str(smallestDistance)
#             return 'Treasure detected at a distance of %s from the sonar device.' % (smallestDistance)
#         else:
#             board[x][y] = 'X'
#             return 'Sonar did not detect anything. All treasure chests out of range.'

# def enterPlayerMove(previousMoves):
#     # Let the player enter their move. Return a two-item list of int xy coordinates.
#     print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
#     while True:
#         move = input()
#         if move.lower() == 'quit':
#             print('Thanks for playing!')
#             sys.exit()

#         move = move.split()
#         if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
#             if [int(move[0]), int(move[1])] in previousMoves:
#                 print('You already moved there.')
#                 continue
#             return [int(move[0]), int(move[1])]

#         print('Enter a number from 0 to 59, a space, then a number from 0 to 14.')

# def showInstructions():
#     print('''Instructions:
# You are the captain of the Simon, a treasure-hunting ship. Your current mission
# is to use sonar devices to find three sunken treasure chests at the bottom of
# the ocean. But you only have cheap sonar that finds distance, not direction.

# Enter the coordinates to drop a sonar device. The ocean map will be marked with
# how far away the nearest chest is, or an X if it is beyond the sonar device's
# range. For example, the C marks are where chests are. The sonar device shows a
# 3 because the closest chest is 3 spaces away.

# 1 2 3
# 012345678901234567890123456789012

# 0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
# 1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
# 2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
# 3 ````````~~~`````~~~`~`````~`~``~` 3
# 4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

# 012345678901234567890123456789012
# 1 2 3
# (In the real game, the chests are not visible in the ocean.)

# Press enter to continue...''')
#     input()

#     print('''When you drop a sonar device directly on a chest, you retrieve it and the other
# sonar devices update to show how far away the next nearest chest is. The chests
# are beyond the range of the sonar device on the left, so it shows an X.

# 1 2 3
# 012345678901234567890123456789012

# 0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
# 1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
# 2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
# 3 ````````~~~`````~~~`~`````~`~``~` 3
# 4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

# 012345678901234567890123456789012
# 1 2 3

# The treasure chests don't move around. Sonar devices can detect treasure chests
# up to a distance of 9 spaces. Try to collect all 3 chests before running out of
# sonar devices. Good luck!

# Press enter to continue...''')
#     input()



# print('S O N A R !')
# print()
# print('Would you like to view the instructions? (yes/no)')
# if input().lower().startswith('y'):
#     showInstructions()

# while True:
#     # Game setup
#     sonarDevices = 20
#     theBoard = getNewBoard()
#     theChests = getRandomChests(3)
#     drawBoard(theBoard)
#     previousMoves = []

#     while sonarDevices > 0:
#         # Show sonar device and chest statuses.
#         print('You have %s sonar device(s) left. %s treasure chest(s) remaining.' % (sonarDevices, len(theChests)))

#         x, y = enterPlayerMove(previousMoves)
#         previousMoves.append([x, y]) # We must track all moves so that sonar devices can be updated.

#         moveResult = makeMove(theBoard, theChests, x, y)
#         if moveResult == False:
#             continue
#         else:
#             if moveResult == 'You have found a sunken treasure chest!':
#                 # Update all the sonar devices currently on the map.
#                 for x, y in previousMoves:
#                     makeMove(theBoard, theChests, x, y)
#             drawBoard(theBoard)
#             print(moveResult)

#         if len(theChests) == 0:
#             print('You have found all the sunken treasure chests! Congratulations and good game!')
#             break

#         sonarDevices -= 1

#     if sonarDevices == 0:
#         print('We\'ve run out of sonar devices! Now we have to turn the ship around and head')
#         print('for home with treasure chests still out there! Game over.')
#         print(' The remaining chests were here:')
#         for x, y in theChests:
#             print(' %s, %s' % (x, y))

#     print('Do you want to play again? (yes or no)')
#     if not input().lower().startswith('y'):
#         sys.exit()
