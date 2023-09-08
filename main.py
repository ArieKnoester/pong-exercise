from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from net_segment import NetSegment
import time


def initialize_screen():
    new_screen = Screen()
    new_screen.setup(width=800, height=600)
    new_screen.bgcolor("black")
    new_screen.title("Pong")
    new_screen.tracer(0)
    return new_screen


def create_net():
    net_segment_ycor = 265
    for _ in range(9):
        net_segment = NetSegment()
        net_segment.goto(x=0, y=net_segment_ycor)
        net_segment_ycor -= 75


screen = initialize_screen()
end_score = screen.numinput(
    title="Welcome to Python Pong!",
    prompt="Play to what score?",
    default=5
)
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
scoreboard = Scoreboard()
create_net()
ball = Ball()

# screen.listen() must be set after screen.numinput()
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_running = True
while game_running:
    screen.update()

    time.sleep(0.1)
    ball.move()

    # Detect if ball collides with either paddle.
    if (
        (
            330 < ball.xcor() < 360
            and ball.distance(right_paddle) < 50
        )
        or
        (
            -330 > ball.xcor() > -360
            and ball.distance(left_paddle) < 50
        )
    ):
        ball.paddle_bounce()

    if not ball.in_play:
        side_out = ball.side_out
        scoreboard.add_point_to_score(side_out)
        ball = Ball()

    if scoreboard.left_score == end_score or scoreboard.right_score == end_score:
        game_running = False

screen.exitonclick()
