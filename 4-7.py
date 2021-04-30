from itertools import count
from math import factorial

def my_func():
    for el in count(1):
        yield factorial(el)

n = 0
for el in my_func():
    if n < 6:
        print(el)
        n += 1