class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self._current_speed = 0

    def go(self):
        self._current_speed = self.speed
        print(f"{self.name} поехала")

    def stop(self):
        self._current_speed = 0
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.name}: {self._current_speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self._current_speed > 60:
            print("Превышение скорости!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self._current_speed > 40:
            print("Превышение скорости!")


class PoliceCar(Car):
    pass


car = Car(100, "red", "Машина")
car.go()
car.show_speed()
car.turn("направо")
car.stop()

town_car = TownCar(70, "yellow", "Городская машина")
town_car.go()
town_car.show_speed()

work_car = WorkCar(50, "green", "Рабочая машина")
work_car.go()
work_car.show_speed()

police_car = PoliceCar(120, "blue", "Полицейская машина", True)
police_car.go()
police_car.show_speed()
