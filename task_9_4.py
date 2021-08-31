class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Машина поехала...')
    def stop(self):
        print('Машина остановилась...')
    def turn(self):
        print('Машина повернула...')
    def show_speed(self):
        print(f'Скорость машины {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости {self.speed}')
        else:
            print(f'Скорость машины {self.speed}')

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости {self.speed}')
        else:
            print(f'Скорость машины {self.speed}')

class PoliceCar(Car):
    pass

class SportCar(Car):
    pass

towncar = TownCar(50, 'red', 'polo', False)
workcar = WorkCar(50, 'red', 'polo', False)

towncar.go()
towncar.show_speed()
towncar.turn()
towncar.stop()

workcar.go()
workcar.show_speed()
workcar.turn()
workcar.stop()

