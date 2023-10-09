from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.x_move = 10
        self.y_move = 10

    def movement(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x=x_cor, y=y_cor)

    def collisionWall(self):
        self.y_move *= -1

    def collisionPad(self):
        self.x_move *= -1

    def reset_position_ball(self):
        self.home()
        self.x_move *= -1
