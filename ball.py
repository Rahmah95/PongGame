# Pong - Ball class

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1

    def move(self):
        """Move ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounce ball when hit by wall on y-axis"""
        self.y_move *= -1

    def bounce_x(self):
        """Bounce ball when hit by paddle on x-axis"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset ball to starting position"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

