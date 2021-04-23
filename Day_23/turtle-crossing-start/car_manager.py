from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
INITIAL_POSITION = (300, -280)


class CarManager(Turtle):
    def __init__(self, y_cord, x_cord):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.y_cord = y_cord
        self.x_cord = x_cord
        self.initial_x = x_cord
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(self.initial_x, self.y_cord)

    def move(self):
        if self.xcor() < -320:
            self.goto(320, self.y_cord)
        new_x = self.xcor() - self.speed
        self.goto(new_x, self.y_cord)

    def level_up(self):
        self.speed += MOVE_INCREMENT
