# Pong - ScoreBoard class
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.create_scoreboard()
        self.score = 0

    def create_scoreboard(self):
        """Create scoreboard"""
        self.color("white")
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        """Update scoreboard with current score on screen"""
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """Increase score by 1"""
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def score_position_player1(self):
        """Position score on screen  for player 1"""
        self.goto(200, 265)
        self.update_scoreboard()

    def score_position_player2(self):
        """Position score on screen for player 2"""
        self.goto(-200, 265)
        self.update_scoreboard()
