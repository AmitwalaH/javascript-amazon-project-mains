# A

# file = open("ex.txt", "r")

# content = file.read()

# print(content)
# file.close()



# B
# text = "Dunder Mifflin - The Paper CO."

# file = open("ex.txt", "a")
# file.write(text + "\n")
# file.close()

# file = open("ex.txt", "r")
# content = file.read()
# print(content)
# file.close()




# C
file_name = "ex.txt"
n = 1

print("Amit Wala")
print("53003230039")

file = open(file_name, "r")
lines = file.readlines()
file.close()

last_lines = lines[-n:]

for line in last_lines:
    print(line, end="")



# D
# class Student:
#     def __init__(self, name, roll, grade):
#         self.name = name
#         self.roll = roll
#         self.grade = grade

#     def display_info(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll)
#         print("Grade:", self.grade)

# student1 = Student("Amit Wala", 53003230039, "A")
# student1.display_info()



# E
# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def sound(self):
#         print(self.name + " barks.")

# print("Amit Wala")        
# print("53003230039")        

# dog1 = Dog("Buddy")
# dog1.sound()




# F
# def greet(name):
#     return f"Hello, {name}!"

# def add(a, b):
#     return a + b

# import py3

# message = py3.greet("Amit")
# print(message)

# result = py3.add(5, 3)
# print("Sum:", result)



# G
# print("Amit Wala")
# print("53003230039")
# try:    
#     number = int(input("Enter a number: "))    
#     result = 10 / number    
#     print("Result:", result)
# except ZeroDivisionError:    
#     print("Error: You cannot divide by zero.")
# except ValueError:    
#     print("Error: Invalid input. Please enter a number.")
# else:
#     print("Result:", result)    



# H
# import tkinter as tk

# root = tk.Tk()
# root.title("Configured Widget Example")


# label = tk.Label(root, text="Hello, Amit Wala - 39!", bg="red", font=("Times", 18))

# label.pack(padx=20, pady=20)

# root.mainloop()



# I
# import tkinter as tk

# root = tk.Tk()
# root.title("Tkinter Widgets Example")

# message = tk.Message(root, text="Amit Wala", bg="lightblue", font=("Arial", 14))
# message.pack(padx=10, pady=10)

# button = tk.Button(root, text="Click Me", bg="green", fg="white", font=("Arial", 12))
# button.pack(padx=10, pady=10)

# entry = tk.Entry(root, bg="white", font=("Arial", 12))
# entry.pack(padx=10, pady=10)

# checkbutton = tk.Checkbutton(root, text="Check me", bg="lightgray", font=("Arial", 12))
# checkbutton.pack(padx=10, pady=10)

# radiobutton1 = tk.Radiobutton(root, text="Option 1", value=1, bg="lightyellow", font=("Arial", 12))
# radiobutton1.pack(padx=10, pady=5)

# radiobutton2 = tk.Radiobutton(root, text="Option 2", value=2, bg="lightyellow", font=("Arial", 12))
# radiobutton2.pack(padx=10, pady=5)


# root.mainloop()
