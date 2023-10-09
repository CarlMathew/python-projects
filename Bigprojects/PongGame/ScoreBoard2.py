from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.player = 0
        self.ht()
        self.penup()
        self.color("white")
        self.Player_Score()


    def Player_Score(self):
        self.goto(self.pos)
        self.write(self.player, move=False, align="center", font=("Courier", 35, "bold"))


    def add_score_1(self):
        self.clear()
        self.player += 1
        self.write(self.player, move=False, align="center", font=("Courier", 35, "bold"))


