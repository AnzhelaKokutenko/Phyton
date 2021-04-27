def my_func(a, b, c):
    x = [a, b, c]
    x.remove(min(a, b, c))
    return sum(x)
print(my_func(9, 1, 5))
