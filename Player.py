from turtle import Turtle


class player(Turtle):
    move_size = 15

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("lime")
        self.shape("turtle")
        self.shapesize(stretch_wid=1.2,stretch_len=1.2)
        self.setpos(0, -250)
        self.setheading(90)
        self.showturtle()

    def move(self):
        self.forward(self.move_size)

    def getY(self):
        return self.position()[1]

    def getAllPositions(self):
        return self.position()

    def sploosh(self):
        self.shape("square")

    def deletePlayer(self):
        self.reset()
        self.hideturtle()
        del self


