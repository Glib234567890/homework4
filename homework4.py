class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start_engine(self):
        return "Двигун завівся з кінською силою: " + str(self.horsepower)


class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def roll(self):
        return f"Машина їде на {self.wheel_count} колесах."


class Car(Engine, Wheels):
    def __init__(self, horsepower, wheel_count, brand):
        Engine.__init__(self, horsepower)
        Wheels.__init__(self, wheel_count)
        self.brand = brand

    def show_details(self):
        return f"Марка машини: {self.brand}, {self.start_engine()}, {self.roll()}"


my_car = Car(360, 4, "Mercedes")
print(my_car.show_details())
