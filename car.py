from turtle import Turtle
from random import randint


class Car(Turtle):
    colours = ["green","yellow", "red", "blue", "violet", "magenta","orange", "cyan", "brown"]
    xPos = 250
    moveSize = 0
    cDis = 20

    def __init__(self, xDiff, posy, mSize):
        super().__init__()
        self.moveSize = mSize
        self.hideturtle()
        self.speed(0)
        turCol = self.colours[randint(0, 8)]
        self.color(turCol)
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.setposition(self.xPos + xDiff, posy)
        self.shapesize(stretch_wid=0.5, stretch_len=1.5)
        self.showturtle()

    def move(self):
        self.forward(self.moveSize)

    def xPosition(self):
        return self.position()[0]

    def deleteCar(self):
        self.reset()
        self.hideturtle()
        del self

    def tooClose(self, pPos):
        if self.distance(pPos[0], pPos[1]) < 20:
            return True
        else:
            return False