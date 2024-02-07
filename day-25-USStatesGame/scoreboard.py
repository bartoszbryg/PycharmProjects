from turtle import Turtle

FONT1 = ("Arial", 30, "normal")
FONT2 = ("Arial", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.attempts = 0

        self.hideturtle()
        self.penup()
        self.pencolor("black")
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"Score: {self.score}/50", align=ALIGNMENT, font=FONT1)
        self.goto(250, 200)
        self.write(f"Nr of attempts: {self.attempts}", align=ALIGNMENT, font=FONT2)

    def change_score(self):
        self.score += 1
        self.attempts += 1
        self.update_screen()

    def already_guessed(self):
        self.update_screen()
        self.goto(0, 50)
        self.write("Already guessed!", align=ALIGNMENT, font=FONT1)

    def bad_guess(self):
        self.attempts += 1
        self.update_screen()
        self.goto(0, 50)
        self.write("Bad guess :(", align=ALIGNMENT, font=FONT1)

    def win(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Congratulation! You've won after {self.attempts} attempts!", align=ALIGNMENT, font=FONT2)
