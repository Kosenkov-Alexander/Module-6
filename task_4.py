'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево)
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_info(self):
        return f'Цвет машины: {self.color}, марка машины: {self.name}, полицейский авто: {self.is_police}'
    def show_speed(self):
        return f'Текущая скорость автомобиля: {self.speed} км/час'
    def go(self):
        return f'Поехала'
    def stop(self):
        return f'Остановилась'
    def turn(self):
        return f'Повернула'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return 'Вы превысили скорость!'
        else:
            return f'Текущая скорость автомобиля: {self.speed} км/час'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return 'Вы превысили скорость!'
        else:
            return f'Текущая скорость автомобиля: {self.speed} км/час'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

town_c = TownCar(50, 'Красный', 'BMW', False)
print(town_c.show_info())
print(town_c.show_speed())

sport_c = SportCar(80, 'Синий', 'Mazda', False)
print(sport_c.show_info())
print(sport_c.show_speed())

work_c = WorkCar(80, 'Зелёный', 'Kio Rio', False)
print(work_c.show_info())
print(work_c.show_speed())

police_c = PoliceCar(80, 'Фиолетовый', 'УАЗ', True)
print(police_c.show_info())
print(police_c.show_speed())