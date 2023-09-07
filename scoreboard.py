from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Tahoma", 32, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        # self.goto(position)
        self.goto(x=0, y=240)
        # self.score = 0
        self.left_score = 0
        self.right_score = 0
        self.display_score()

    def add_point_to_score(self, side_out):
        if side_out == "right":
            self.left_score += 1
        elif side_out == "left":
            self.right_score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(
            f"{self.left_score}                       {self.right_score}",
            align=ALIGNMENT,
            font=FONT)