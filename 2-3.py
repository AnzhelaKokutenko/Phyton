period = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
a = int(input('Введите число от 1 до 12: '))
for key, value in period.items():
        if a in value:
            print(key)
