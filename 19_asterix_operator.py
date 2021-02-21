print('multiplication')
print(2 * 4)
print('power')
print(2 ** 4)
print('Repeat strings, tuples or lists')
print(('a', 'b') * 7, [1, 2] * 2, 'ccc' * 3)

print('Unpacking')
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
start, *middle, pre_last, last = numbers  # unpacking creates always a list
print(start, middle, pre_last, last)

print('Merging iterables (sets, tuples, list)')
tuple1 = 1,2,3
list1 = [4,5,6]
list2 = [*tuple1, *list1]
tuple2 = (*list1, *tuple1)
print(list2)
print(tuple2)

print('Merging dictionaries')
dict1 = {'a': 1, 'b': 2}
dict2 = dict(b=3, c=4)
print({**dict1, **dict2})

print('Other stuff: 18: Function Arguments')
