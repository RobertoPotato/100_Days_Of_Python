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
scoreboard = Scoreboard()

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
            scoreboard.game_over()

    # Detect finished crossing
    if player.is_at_finish():
        scoreboard.increase_level()
        player.reposition()
        for car in CARS:
            car.level_up()
        print(CARS[0].speed)

screen.exitonclick()
