class Storage:
    pass

class Equipment:
    def __init__(self, name, quantity, price):
        self.n = name
        self.q = quantity
        self.p = price

    @classmethod
    def getstorage(cls):
        while True:
            try:
                a = input(f'Введите наименование ')
                b = int(input(f'Введите цену за ед '))
                c = int(input(f'Введите количество '))
                new = {'Модель ':a, 'Цена за ед': b, 'Количество': c}
                print(f'Текущий список -\n {new}')
            except:
                return f'Ошибка ввода данных'
            q = input(f'Выход?')
            if q == 'y':
                return f'Выход'

class Printer(Equipment):
    @property
    def __str__(self):
        return f'На складе в наличии Принтер {self.n} в количестве {self.q} по цене за шт {self.p}'


class Scaner(Equipment):
    @property
    def __str__(self):
        return f'На складе в наличии Сканер {self.n} в количестве {self.q} по цене за шт {self.p}'


class Xerox(Equipment):
    @property
    def __str__(self):
        return f'На складе в наличии Ксерокс {self.n} в количестве {self.q} по цене за шт {self.p}'


p = Printer('HP', '10', '5000')
s = Scaner('Samsung', '20', '7000')
x = Xerox('Xerox', '30', '8000')

print(p.__str__)
print(s.__str__)
print(x.__str__)

print(Equipment.getstorage())
