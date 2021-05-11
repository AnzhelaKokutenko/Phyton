try:
    with open('test_5.txt', 'w') as f:
        numb = input('Введите цифры через пробел \n')
        f.writelines(numb)
        my_numb = numb.split()

        print(sum(map(int, my_numb)))
except IOError:
    print('Ошибка')
except ValueError:
    print('Ошибка')