from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        self.score = 0
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in POSITION:
            self.add_segments(position)

    def add_segments(self, pos):
        seg = Turtle("square")
        seg.penup()
        seg.color("white")
        seg.goto(x=pos[0], y=pos[1])
        self.segments.append(seg)

    def extendSnake(self):
        self.add_segments(self.segments[-1].position())

    def MovingUp(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def MovingLeft(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def MovingDown(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def MovingRight(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def snakeMoving(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x_value = self.segments[i - 1].xcor()
            y_value = self.segments[i - 1].ycor()

            self.segments[i].goto(x=x_value, y=y_value)
        self.segments[0].forward(20)

    def reset_everything(self):
        for seg in self.segments:
            seg.goto(x=5000, y=5000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]