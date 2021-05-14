from abc import ABC, abstractmethod
class Clothes(ABC):

    def __init__(self, arg):
        self.arg = arg

    @property
    def costs(self):
        return f'Сумма затраченной ткани равна: {(self.arg / 6.5 + 0.5) + (2 * self.arg+ 0.3) :.2f}'

    @abstractmethod
    def my_method(self):
        return 'Это одежда'

class Coat(Clothes):
    def get_coat(self):
        return f'Для пошива пальто нужно: {round(self.arg / 6.5 + 0.5)} м ткани'

    def my_method(self):
        return 'Это пальто'

class Suit(Clothes):
    def get_suit(self):
        return f'Для пошива костюма нужно: {round(2 * self.arg + 0.3)/100 } м ткани'

    def my_method(self):
        return 'Это костюм'
        pass

coat = Coat(40)
cos = Suit(178)
print(coat.get_coat())
print(cos.get_suit())
print(coat.my_method())
print(cos.my_method())
