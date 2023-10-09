from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()

# Movements setup
screen.listen()
screen.onkey(key="Up", fun=snake.MovingUp)
screen.onkey(key="Left", fun=snake.MovingLeft)
screen.onkey(key="Down", fun=snake.MovingDown)
screen.onkey(key="Right", fun=snake.MovingRight)

# Adding the food of the snake
food = Food()


def recording_score():
    with open("myhighscore.txt", mode="w") as myScore:
        myScore.write(str(scoreBoard.high_score))


# Inserting the ScoreBoard
scoreBoard = ScoreBoard()
gameOn = True
while gameOn:
    screen.update()
    time.sleep(0.06)

    snake.snakeMoving()

    if snake.segments[0].distance(food) < 15:
        food.random_positions()
        snake.extendSnake()
        scoreBoard.add_score()

    elif snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 \
            or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreBoard.reset_score()
        snake.reset_everything()
        recording_score()

    # Detect collision with tail

    for myseg in snake.segments[1:]:
        # if myseg == snake.segments[0]:
        #     pass
        if snake.segments[0].distance(myseg) < 10:
            scoreBoard.reset_score()
            snake.reset_everything()
            recording_score()
screen.exitonclick()
