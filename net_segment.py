from turtle import Turtle


class NetSegment(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1.75, stretch_len=0.5)
        self.penup()
