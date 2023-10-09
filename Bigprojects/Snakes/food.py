from turtle import Turtle
import random





class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.penup()
        self.random_positions()

    def random_positions(self):
        x_value = random.randint(a=-250, b=250)
        y_value = random.randint(a=-250, b=250)
        self.goto(x=x_value, y=y_value)

