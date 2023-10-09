import time
from turtle import Screen
from userPaddle import Paddle
from ball import Ball
from time import sleep
from ScoreBoard2 import ScoreBoard
speed = 0.09
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong Game")
pads = Paddle((375, 0))
pads2 = Paddle((-375, 0))
balls = Ball()
score1 = ScoreBoard((50, 250))
score2 = ScoreBoard((-50, 250))
screen.listen()

screen.onkey(fun=pads.moveUp, key="Up")
screen.onkey(fun= pads.moveDown, key = "Down")
screen.onkey(fun=pads2.moveUp, key="w")
screen.onkey(fun= pads2.moveDown, key = "s")
while True:
    screen.update()
    sleep(speed)
    balls.movement()

    if balls.ycor() == 290 or balls.ycor() == -290:
        balls.collisionWall()
        speed -= 0.005
    elif pads.distance(balls) < 50 and balls.xcor() > 350 or pads2.distance(balls) < 50 and balls.xcor() < -350:
        balls.collisionPad()
        speed -= 0.005


    elif balls.xcor() > 400:
        score2.add_score_1()
        balls.reset_position_ball()
        speed = 0.09

    elif balls.xcor() < -400:
        balls.reset_position_ball()
        score1.add_score_1()
        speed = 0.09










screen.exitonclick()