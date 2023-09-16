# Pong - main.py

# Import libraries and classes

from turtle import Screen, Turtle
from scoreboard import ScoreBoard
from paddles import Paddle
from ball import Ball
import time

#####################

# create objects from classes
screen = Screen()
screen_split = Turtle()
score_P1 = ScoreBoard()
score_P2 = ScoreBoard()
paddle_P1 = Paddle()
paddle_P2 = Paddle()
ball = Ball()


####################
# declaration of functions
def screen_setup():
    """Setup screen"""
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)


def split_screen():
    """Split screen into two"""
    screen_split.hideturtle()
    screen_split.penup()
    screen_split.goto(0, -280)
    screen_split.left(90)
    screen_split.color("white")
    for i in range(19):
        screen_split.pendown()
        screen_split.forward(15)
        screen_split.penup()
        screen_split.forward(20)


def objects_layout_setup():
    """Setup objects position on screen"""
    paddle_P1.paddle_position(360, 0)
    paddle_P2.paddle_position(-360, 0)
    score_P1.score_position_player1()
    score_P2.score_position_player2()


def event_listener_for_player1():
    """Move player 1 paddle with keyboard"""
    screen.onkeypress(paddle_P1.paddle_move_up, "Up")
    screen.onkeypress(paddle_P1.paddle_move_down, "Down")


def event_listener_for_player2():
    """Move player 2 paddle with keyboard"""
    screen.onkeypress(paddle_P2.paddle_move_up, "w")
    screen.onkeypress(paddle_P2.paddle_move_down, "s")


def conditions_tracking():
    """Score and game conditions tracking"""
    # detect ball collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    ##################################
    # detect ball collision with player1/right paddle
    if ball.distance(paddle_P1) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        print("made contact")

    # detect ball collision with player2/left paddle
    if ball.distance(paddle_P2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        print("made contact")
    ##################################
    # detect if player 1/right paddle misses the ball
    if ball.xcor() >= 400:
        score_P2.increase_score()
        ball.reset_position()

    # detect if player 2/left paddle misses the ball
    if ball.xcor() <= -400:
        score_P1.increase_score()
        ball.reset_position()


def game_loop():
    """Move objects"""
    screen.listen()
    event_listener_for_player1()
    event_listener_for_player2()
    game_on = True
    while game_on:
        time.sleep(0.1)  # to slow ball movement
        screen.update()
        ball.move()
        conditions_tracking()


#################

# Execute program
screen_setup()
split_screen()
objects_layout_setup()
game_loop()
screen.exitonclick()
