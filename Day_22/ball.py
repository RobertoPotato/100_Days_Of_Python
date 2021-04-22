from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("lime")
        self.shape("circle")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.y_movement = 10
        self.x_movement = 10
        self.move_speed = 0.1

    def update_position(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
