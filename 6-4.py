class Car:
    def __init__(self,name, color, speed):
        self.s = speed
        self.c = color
        self.n = name
    def go(self):
        print(f'{self.n} поехала')
    def stop(self):
        print(f'{self.n} остановилась')
    def turn(self):
        print(f'{self.n} повернула')
    def show_speed(self):
        print(f'Скорость {self.n} составляет {self.s} ')
class TownCar(Car):
    def show_speed(self):
        print(f'Скорость {self.n} составляет {self.s} {"Скорость превышена" if self.s > 60 else "скорость ок"}')
class SportCar(Car):
    def show_speed(self):
        print(f'Скорость {self.n} составляет {self.s} ')
class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость {self.n} составляет {self.s} {"Скорость превышена" if self.s>40 else"скорость ок"}')
class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        self.p = is_police
        super().__init__(name, color, speed)

tcar = TownCar('taxi','yellow', 70)
scar = SportCar('Lamba', 'red',200)
wcar = WorkCar('bus', 'grey', 50)
pcar = PoliceCar('police','black',80)

tcar.go()
pcar.stop()
scar.show_speed()
tcar.show_speed()