from random import randint


class Ball:
    def __init__(self, color, pos_x, pos_y, size):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size

    def getColor(self):
        return self.color

    def getPosX(self):
        return self.pos_x

    def getPosY(self):
        return self.pos_y

    def getSize(self):
        return self.size

    def moveBall(self, move_x, move_y):
        self.pos_x += move_x
        self.pos_y -= move_y

    def checkCollision(self, window_w, window_h, velocity=[]):
        if self.pos_x + self.size > window_w or self.pos_x < 0:
            velocity[0] = -velocity[0]
            color = (randint(0, 255), randint(0, 255), randint(0, 255))

        if self.pos_y + self.size > window_h or self.pos_y < 0:
            velocity[1] = -velocity[1]
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
