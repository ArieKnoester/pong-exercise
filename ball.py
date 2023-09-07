from turtle import Turtle
import random
MOVE_SPEED = 25


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.setheading(45)
        self.in_play = True
        self.side_out = ""
        self.set_initial_trajectory()

    def move(self):
        self.forward(MOVE_SPEED)

        if self.ycor() > 280 or self.ycor() < -280:
            self.wall_bounce()
        self.check_ball_in_play()

    def check_ball_in_play(self):
        if self.xcor() > 420:
            self.in_play = False
            self.side_out = "right"
        if self.xcor() < -420:
            self.in_play = False
            self.side_out = "left"

    def wall_bounce(self):
        current_heading = self.heading()
        new_heading = 360 - current_heading
        self.setheading(new_heading)

    def paddle_bounce(self):
        current_heading = self.heading()
        new_heading = 180 - current_heading
        self.setheading(new_heading)

    def set_initial_trajectory(self):
        service_side = random.choice(("left", "right"))
        heading = 0

        if service_side == "left":
            heading = random.randrange(120, 261)
        elif service_side == "right":
            heading = random.randrange(-70, 70)

        self.setheading(heading)
