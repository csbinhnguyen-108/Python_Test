class Ball:
    def __init__(self, color, pos_x, pos_y, ):
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y

    def getName(self):
        return self.color

    def getPosX(self):
        return self.pos_x

    def getPosY(self):
        return self.pos_y
