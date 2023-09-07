from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -250:
            self.backward(MOVE_DISTANCE)
