def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return 'На ноль делить нельзя'

x = float(input('Введите аргумент x: '))
y = float(input('Введите аргумент y: '))
print(divide(x, y))
