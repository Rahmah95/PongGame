from turtle import Turtle
import time


class Timer(Turtle):
    def __init__(self):
        super().__init__()
        self.create_timer()
        self.time_count_down = 3500  # time in seconds

    def create_timer(self):
        """Create scoreboard"""
        self.color("white")
        self.penup()
        self.hideturtle()

    def countdown(self):
        """Countdown timer"""
        if self.time_count_down > 0:
            mins, secs = divmod(self.time_count_down, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.time_count_down -= 1
            return timer
        else:
            return "00:00"

    def update_timer(self):
        """Update scoreboard with current score on screen"""
        self.write(f"Time: {self.countdown()}", align="center", font=("Arial", 24, "normal"))

    def timer_position(self):
        """Position time on screen"""
        self.goto(0, 265)
        self.update_timer()
