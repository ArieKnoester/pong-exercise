from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Tahoma", 32, "normal")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(position)
        self.score = 0
        self.display_score()

    def add_point_to_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)