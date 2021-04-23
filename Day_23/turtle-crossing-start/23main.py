import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

START_LOCATIONS = [0, 50, 100, 150, 200, 250, -50, -100, -150, -200, -250]
CARS = []

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()

screen.onkeypress(player.move, "Up")


def generate_cars():
    for i in range(0, 50):
        CARS.append(CarManager(y_cord=random.choice(START_LOCATIONS), x_cord=random.randint(-280, 280)))


generate_cars()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in CARS:
        car.move()

    # Detect collision with car
    for car in CARS:
        if car.distance(player) < 20:
            game_is_on = False

    # Detect finished crossing
    if player.is_at_finish():
        player.reposition()

screen.exitonclick()

# HAVE different tracks and on each track, generate cars on different x-axis positions.
# Tracks will be created along the y direction
# Cars will be generated randomly on the tracks
# Once a car reaches the end of the screen, it gets repositioned back to the begining
# Also have a variable that controls the speed of the animation each time the player advances
# A level
