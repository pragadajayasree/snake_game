from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_file.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.color("white")
        self.in_score()

    def in_score(self):
        self.clear()
        self.write(f"score = {self.score}  High score = {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_file.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.in_score()

    """ def game_over(self):
        self.home()
        self.write("Game over", align=ALIGN, font=FONT)"""

    def inc_score(self):
        self.score += 1
        self.in_score()
