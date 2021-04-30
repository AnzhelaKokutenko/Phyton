from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

print('------------------------')

с = 0
for el in cycle([0, 1, True, False]):
    if с == 10:
        break
    print(el)
    с += 1
