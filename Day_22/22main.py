import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_player = Paddle(coordinates=(350, 0))
l_player = Paddle(coordinates=(-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_player.go_up, "Up")
screen.onkey(r_player.go_down, "Down")

screen.onkey(l_player.go_up, "w")
screen.onkey(l_player.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.update_position()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right and left paddles
    if ball.distance(r_player) < 50 and ball.xcor() > 320 or ball.distance(l_player) < 50 and ball.xcor() < -320:
        print("MADE CONTACT")
        ball.bounce_x()

    # Detect right paddle miss
    if ball.xcor() > 385:
        scoreboard.l_point()
        ball.reset_position()

    # Detect left paddle miss
    if ball.xcor() < -385:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()
