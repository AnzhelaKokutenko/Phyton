num = int(input("Введите натуральное число: "))
my_list = [7, 5, 3, 3, 2]
for el in my_list:
        if num > el:
            i = my_list.index(el)
            my_list.insert(i, num)
            break
        elif num < my_list[len(my_list) - 1]:
            my_list.append(num)
print(my_list)