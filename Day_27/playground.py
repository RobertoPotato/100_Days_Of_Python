
def add(*args):
    sum_ = 0
    for n in args:
        sum_ += n
    return sum_


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

    def get_details(self):
        print(f"Make: {self.make}\nModel: {self.model}")


my_car = Car(make="Jeep", model="Wrangler Rubicon")
my_car.get_details()
