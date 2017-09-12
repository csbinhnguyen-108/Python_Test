from tkinter import *
from tkinter import messagebox
import pygame
from random import randint

pygame.init()

window_w = 800
window_h = 600

white = (255, 255, 255)
black = (0, 0, 0)


FPS = 120

window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("Game: ")
clock = pygame.time.Clock()


def game_loop():

    block_size = 20

    velocity = [3, 3]

    pos_x = window_w/2
    pos_y = window_h/2
    color = (255, 255, 255)
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pos_x += velocity[0]
        pos_y += velocity[1]

        if pos_x + block_size > window_w or pos_x < 0:
            velocity[0] = -velocity[0]
            color = (randint(0, 255), randint(0, 255), randint(0, 255))

        if pos_y + block_size > window_h or pos_y < 0:
            velocity[1] = -velocity[1]
            color = (randint(0, 255), randint(0, 255), randint(0, 255))

        # DRAW
        window.fill(black)
        pygame.draw.rect(window, color, [pos_x, pos_y, block_size, block_size])
        pygame.display.update()
        clock.tick(FPS)


game_loop()
'''Pygame Moving Rectangle Test
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

    move = 5
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y -= move
    if pressed[pygame.K_DOWN]:
        y += move
    if pressed[pygame.K_LEFT]:
        x -= move
    if pressed[pygame.K_RIGHT]:
        x += move

    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.display.flip()
    clock.tick(60)
'''
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
