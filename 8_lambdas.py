from functools import  reduce

add10 = lambda x: x + 10
mult = lambda a, b: a * b
print(add10(5))
print(mult(10, 3))
print('\n')

points2D = (1, 2), (15, 1), (5, -1), (10, 4)
print(f'Sort after Y:\t\t{sorted(points2D, key=lambda x: x[1])}')
print(f'Sort after X+Y:\t\t{sorted(points2D, key=lambda x: x[0] + x[1])}')
print('\n')

a = 1, 2, 3, 4, 5,6
print(tuple(map(lambda x: x * 2, a)))
print(tuple(x * 2 for x in a)) # equivalent
print('\n')

print(tuple(filter(lambda x: x%2==0, a)))
print('\n')

print(reduce(lambda x,y:x*y,a))
