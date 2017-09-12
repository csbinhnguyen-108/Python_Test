from tkinter import *
from tkinter import messagebox
import pygame

pygame.init()
screen_size = (400, 300)
screen = pygame.display.set_mode(screen_size)
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3
    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3

    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(60)

'''Tkinter Test
class App:
    def __init__(self,master):
        def onClick():
            messagebox.showinfo("Hello", "Hellooooooooooooooo!!!")

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="Quit", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi = Button(frame, text="Hello", fg="green", command=onClick)
        self.hi.pack(side=LEFT)

root = Tk()

app = App(root)

root.mainloop()
'''
''' Calculator
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
