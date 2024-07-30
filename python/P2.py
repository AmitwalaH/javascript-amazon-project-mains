print("Amit Wala")
print("53003230039")
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# current_year = 2024
# year_turn_100 = current_year + (100 - age)
# print(f"Hello {name}! You will turn 100 years old in the year {year_turn_100}.")

# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print(f"The number {number} is even.")
# else:
#     print(f"The number {number} is odd.")

# n = int(input("Enter the number of terms for the Fibonacci series: "))

# a, b = 0, 1
# count = 0

# while count < n:
#     print(a)
#     a, b = b, a + b
#     count += 1

# def reverse_string(value):
#   reversed_value = value[::-1]
#   return reversed_value

# user_input = input("Enter a value to reverse: ")
# result = reverse_string(user_input)
# print(f"The reversed value is: {result}")



# def is_armstrong_number(value):
#   num_str = str(value)
#   num_digits = len(num_str)
#   sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
#   return sum_of_powers == value

# user_input = int(input("Enter a number to check if it is an Armstrong number: "))
# if is_armstrong_number(user_input):
#   print(f"{user_input} is an Armstrong number.")
# else:
#   print(f"{user_input} is not an Armstrong number.")


# def is_palindrome(value):
#   value_str = str(value)
#   return value_str == value_str[::-1]

# user_input = input("Enter a value to check if it is a Palindrome: ")
# if is_palindrome(user_input):
#   print(f"{user_input} is a Palindrome.")
# else:
#   print(f"{user_input} is not a Palindrome.")


# def factorial(n):
#   if n == 0:
#       return 1
#   else:
#       return n * factorial(n - 1)

# user_input = int(input("Enter a number to find its factorial: "))
# result = factorial(user_input)
# print(f"The factorial of {user_input} is {result}.")

# def is_vowel(char):
#   vowels = 'aeiouAEIOU'
#   return char in vowels

# user_input = input("Enter a character to check if it is a vowel: ")
# if len(user_input) == 1:
#   if is_vowel(user_input):
#       print(f"{user_input} is a vowel.")
#   else:
#       print(f"{user_input} is not a vowel.")
# else:
#   print("Please enter only one character.")


# def compute_length(value):
#   return len(value)

# user_input = input("Enter a list or a string (separate elements with spaces for a list): ")
# if ',' in user_input:
#   value = user_input.split(',')
#   length = compute_length(value)
#   print(f"The length of the list is {length}.")
# else:
#   length = compute_length(user_input)
#   print(f"The length of the string is {length}.")



# def histogram(numbers):
#   for num in numbers:
#       print('*' * num)

# numbers = [4, 9, 7]
# histogram(numbers)