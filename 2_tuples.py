import sys
import timeit

tuple1 = 'Max', 28, 'Boston'
tuple2 = 'Chad',
tuple3 = tuple(['foo', 'bar'])

name, age, city = tuple1
print(name, age, city, end=', ')
print('\n')

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple1[-2])

for item in tuple1 + tuple2 + tuple3:
    print(item, end=', ')
print('\n')

tuple5 = 'a', 'p', 'p', 'l', 'e'
print(tuple5.count('p'))
print(tuple5.index('e'))

list1 = list(tuple5)
tuple6 = tuple(list1)

tuple7 = 1,2,3,4,5,6
i1, *i2, i3 = tuple7
print(i1, i2, i3, end=', ')
print('\n')


list2 = [0,1,2, 'Hello', True]
tuple8 = (0,1,2, 'Hello', True)
print(sys.getsizeof(list2), 'bytes')
print(sys.getsizeof(tuple8), 'bytes')

list_stmt = '[{:1}]'.format(','.join(["'{:1}'".format(item) for item in list2]))
tuple_stmt = '({:1})'.format(','.join(["'{:1}'".format(item) for item in tuple8]))
print(timeit.timeit(stmt=list_stmt, number=10000000))
print(timeit.timeit(stmt=tuple_stmt, number=10000000))