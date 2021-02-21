from itertools import product, permutations, \
    combinations, combinations_with_replacement, accumulate, groupby, count, cycle
import operator

set1 = 1, 2
set2 = 3, 4
print(list(product(set1, set2)))

print('Permutations')
set3 = 1, 2, 3, 4, 5, 6
print(list(permutations(set3)))
print(list(permutations(set3, 2)))
print('\n')

print('Combinations')
print(list(combinations(set3, 2)))
print(list(combinations_with_replacement(set3, 2)))
print('\n')

print('Accumulation')
print(list(accumulate(set3)))
print(list(accumulate(set3, func=operator.mul)))
print('\n')

print('Group by')
for k, v in groupby(set3, key=lambda x: x < 3):
    print(f'{k}\t\t{list(v)}')
print('\n')
persons = ({'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 19}, {'name': 'Claire', 'age': 28},
           {'name': 'Rod', 'age': 25}, {'name': 'Hank', 'age': 35},
           {'name': 'Britney', 'age': 28})
for k, v in groupby(persons, key=lambda x: x['age'] ):
    print(f'{k}\t\t{list(v)}')
print('\n')

# print('Count')
# for n in count(10):
#     print(n)

# print('Cycle')
# for i in cycle(set3):
#     print(i)

