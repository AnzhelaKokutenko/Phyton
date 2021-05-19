class MyClass (Exception):

    @staticmethod
    def division(a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return ('На ноль делить нельзя')


x = int(input('Введите число: '))
y = int(input('Введите число: '))
print(MyClass.division(x, y))
