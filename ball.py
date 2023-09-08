from turtle import Turtle
import random
# MOVE_SPEED = 20


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.in_play = True
        self.side_out = ""
        self.move_speed = 20
        self.set_initial_trajectory()

    def move(self):
        self.forward(self.move_speed)

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
        self.increase_ball_movement()

    def paddle_bounce(self):
        current_heading = self.heading()
        new_heading = 180 - current_heading
        self.setheading(new_heading)
        self.increase_ball_movement()

    def increase_ball_movement(self):
        self.move_speed += 1

    def set_initial_trajectory(self):
        service_side = random.choice(("left", "right"))
        heading = 0

        if service_side == "left":
            top_angle = random.randrange(120, 150)
            bottom_angle = random.randrange(210, 240)
            heading = random.choice((top_angle, bottom_angle))
        elif service_side == "right":
            top_angle = random.randrange(30, 60)
            bottom_angle = random.randrange(-60, -30)
            heading = random.choice((top_angle, bottom_angle))

        self.setheading(heading)
