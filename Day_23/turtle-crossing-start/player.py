from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
INITIAL_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("teal")
        self.penup()
        self.goto(INITIAL_POSITION)
        self.setheading(90)

    def move(self):
        self.color("black")
        self.goto(0, self.ycor() + MOVE_DISTANCE)
        print("Moving")

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


    def reposition(self):
        self.goto(INITIAL_POSITION)
