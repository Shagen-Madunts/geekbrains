"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} {self.color} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self):
        print(f"{self.name} развернулась")

    def show_speed(self):
        print(f"Текущая скорость {self.name} {self.speed}")

    def chase(self):
        if self.is_police:
            print(f"Полицейские отправились в погоню за {self.color} {self.name} !")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class TownCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def exceeds_speed_limit(self):
        return self.speed > 60

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color} {self.name} превышает скорость на {self.speed - 40} км/ч !")
        else:
            pass


class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
        self.exceeds_speed_limit()

    def exceeds_speed_limit(self):
        return self.speed > 40

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color} {self.name} превышает скорость на {self.speed - 40} км/ч !")
        else:
            pass


print("\nCar---->")
inst_car = Car("Лада Калина", 100, "Белая", False)
inst_car.go()
inst_car.show_speed()
inst_car.chase()

print("\nTownCar---->")
inst_work_car = TownCar("Мазда", 175, "Красная", True)
inst_work_car.show_speed()
inst_work_car.chase()

print("\nWorkCar---->")
inst_town_car = WorkCar("Камаз", 75, "Желтый", True)
inst_town_car.show_speed()
inst_town_car.chase()
