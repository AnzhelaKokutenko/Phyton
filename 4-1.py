from sys import argv

script_name, hours, stavka, bonus = argv

print("Имя скрипта: ", script_name)
print("Выработка в часах: ", hours)
print("Ставка в час: ", stavka)
print("Премия: ", bonus)
print("Зарплата сотрудника равна: ", (float(hours) * float(stavka)) + float(bonus))
