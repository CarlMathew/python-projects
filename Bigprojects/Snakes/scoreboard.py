from turtle import Turtle

file = open("myhighscore.txt")
SCORE = file.read()
file.close()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(SCORE)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.write(f"Scoreboard:{self.score}, HighScore: {self.high_score}", move=False, align="center",
                   font=("Courier", 12, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"Scoreboard:{self.score}, HighScore: {self.high_score}", move=False, align="center",
                   font=("Courier", 12, "normal"))

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    # def gameOver(self):
    #     self.goto(x=0,y=0)
    #     self.write(f"Game Over!", move=False, align="center", font=("Courier", 24, "bold"))
