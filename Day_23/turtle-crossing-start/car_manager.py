from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
INITIAL_POSITION = (300, -280)


class CarManager(Car):
    def __init__(self):
        super().__init__()
