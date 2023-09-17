# Pong - paddles - Paddle class

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle = self.create_paddle()

    def create_paddle(self):
        """Create paddle"""
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        return self.paddle

    def paddle_position(self, x, y):
        """Position paddle on screen"""
        self.paddle.goto(x, y)

    def paddle_move_up(self):
        """Move paddle up"""
        new_y = self.paddle.ycor() + 20
        if new_y < 270:  # to keep paddle on screen
            self.paddle.goto(self.paddle.xcor(), new_y)

    def paddle_move_down(self):
        """Move paddle down"""
        new_y = self.paddle.ycor() - 20
        if new_y > -260:  # to keep paddle on screen
            self.paddle.goto(self.paddle.xcor(), new_y)

    def paddle_current_position(self):
        """Return current position of paddle"""
        return self.paddle.pos()
