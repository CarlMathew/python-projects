from turtle import Turtle


class Paddle(Turtle, ):
    def __init__(self, position):
        self.pos = position
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.pos)


    def moveUp(self):
        new_y = self.ycor() + 20
        self.goto(x=self.pos[0], y=new_y)

    def moveDown(self):
        new_y = self.ycor()-20
        self.goto(x=self.pos[0], y=new_y)







