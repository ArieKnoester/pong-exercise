from turtle import Screen
from paddle import Paddle
from ball import Ball
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

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
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
    print(f"Ball distance to left_paddle: {ball.distance(left_paddle)}")

    # Detect if ball collides with either paddle.
    # Buggy. Only works if the ball collides with
    # the paddle around the middle of its vertical
    # edge. If the ball collides with the top or bottom
    # of the vertical edge the paddle, it either passes
    # through or gets stuck in the paddle before bouncing.
    if (
        ball.distance(right_paddle) < 25
        or ball.distance(left_paddle) < 25
    ):
        current_heading = ball.heading()
        new_heading = 180 - ball.heading()
        ball.setheading(new_heading)


screen.exitonclick()
