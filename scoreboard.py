from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGHNMENT = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(-270,260)
        self.color("black")
        self.score=1
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.score}",align = ALIGHNMENT, font = FONT)

    def next_level(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0, 0)
        self.write(f"Game Over! Final level: {self.score}", align="center", font=FONT)
