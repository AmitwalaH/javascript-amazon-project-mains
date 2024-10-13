import tkinter as tk

root = tk.Tk()
root.title("Configured Widget Example")


label = tk.Label(root, text="Hello, Amit Wala - 39!", bg="red", font=("Times", 18))

label.pack(padx=20, pady=20)

root.mainloop()