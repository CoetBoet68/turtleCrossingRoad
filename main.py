from turtle import Screen
import Cars
from time import sleep
import Player
from turtle import Turtle


def playerForward():
    player.move()


def update(score, lost= False):
    if not lost:
        scoreboard.penup()
        scoreboard.hideturtle()
        scoreboard.pencolor("white")
        scoreboard.setposition(-270, 270)
        scoreboard.pendown()
        scoreboard.write(f"Level: {score}", align="left", font=("arial", 16, "normal"))
    else:
        scoreboard.penup()
        scoreboard.hideturtle()
        scoreboard.pencolor("white")
        scoreboard.setposition(0,0)
        scoreboard.pendown()
        scoreboard.write(f"Game Over! Your score is: {score}", align="center", font=("arial", 21, "normal"))

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(playerForward, "Up")
scoreboard = Turtle()
won = True
starter = 3
score = 1
while won:
    update(score)
    player = Player.player()
    cars = Cars.cars()
    winning = True
    cars.startLevel(starter)
    won = False
    while winning and not won:
        cars.createBatch()
        for i in range(8):
            cars.moveBatches()
            cars.removeCars()
            if cars.checkTurtleCrash(player.getAllPositions()):
                winning = False
                won = False
                player.sploosh()
                cars.moveBatches()
                screen.update()
                sleep(2)
                player.deletePlayer()
                cars.deleteAll()
                screen.resetscreen()
                break
            elif player.getY() > 280:
                won = True
                score += 1
                player.deletePlayer()
                cars.deleteAll()
                screen.resetscreen()
                break
            screen.update()
            sleep(0.1)
    starter += 1
update(score, True)
screen.exitonclick()

