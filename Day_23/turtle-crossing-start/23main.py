import random
import time
from turtle import Screen
from player import Player
from player import Player
from car_manager import CarManager
from car import Car
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
    for i in range(0, 200):
        CARS.append(Car(y_cord=random.choice(START_LOCATIONS), x_cord=random.randint(280, 2000)))


generate_cars()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in CARS:
        car.move()

    if player.ycor() > 280:
        player.reposition()
        print("Finished")
