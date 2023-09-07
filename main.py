from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


def initialize_screen():
    new_screen = Screen()
    new_screen.setup(width=800, height=600)
    new_screen.bgcolor("black")
    new_screen.title("Pong")
    new_screen.tracer(0)
    new_screen.listen()
    return new_screen


screen = initialize_screen()
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
left_scoreboard = Scoreboard((-160, 240))
right_scoreboard = Scoreboard((160, 240))
ball = Ball()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_running = True
while game_running:
    screen.update()
    time.sleep(0.2)
    ball.move()

    # Detect if ball collides with either paddle.
    if (
        (ball.xcor() > 330 and ball.distance(right_paddle) < 50)
        or
        (ball.xcor() < -330 and ball.distance(left_paddle) < 50)
    ):
        ball.paddle_bounce()

    # Scoring. I don't like how I'm repeating code in these conditionals.
    if ball.xcor() > 420:
        left_scoreboard.add_point_to_score()
        ball = Ball()
    if ball.xcor() < -420:
        right_scoreboard.add_point_to_score()
        ball = Ball()

screen.exitonclick()
