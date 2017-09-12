import tkinter
from tkinter import messagebox

top = tkinter.Tk()


def helloCallBack():
    messagebox.showinfo("Hello", "Hello World")

B = tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()

top.mainloop()

'''
# Add two numbers
def add(num1, num2):
    return num1 + num2


# Subtract two numbers
def subtract(num1, num2):
    return num1 - num2


# Multiply two numbers
def multiply(num1, num2):
    return num1 * num2


# Divide two numbers
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero!"
    else:
        return num1 / num2


# Modulo two numbers
def modulus(num1, num2):
    return num1 % num2


# Stores user choice
choice = input("Select a command (1-5): ")

# Prompts user to input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Checks choice
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == '5':
    print(num1, "%", num2, "=", modulus(num1, num2))
else:
    print("Invalid Input")
'''
