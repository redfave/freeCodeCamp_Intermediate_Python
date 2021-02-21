from copy import copy, deepcopy

print('Immutable reassignment')
num_original =5
print(f'Original:\t\t\t\t\t\t{num_original}')
num_copy = num_original
num_copy = 7 # A new assignment as integers are immutable
print(f'Original after reassignment:\t{num_original}')
print(f'Copy:\t\t\t\t\t\t\t{num_copy}')
print('\n')

print('Mutable reassignment')
list_original = [1,2,3,4,5]
print(f'Original:\t\t\t\t\t\t{list_original}')
list_copy = list_original
list_copy[0] = 99
print(f'Original after reassignment:\t{list_original}')
print(f'Copy:\t\t\t\t\t\t\t{list_copy}')
print('\n')

print('Shallow copy')   # Copies only references in nested properties
list_shallow = copy(list_original)
# shallow copy alternatives
# list_shallow = list_original.copy()
# list_shallow = list(list_original)
# list_shallow = list_shallow[:]
list_shallow[0] = 'foo'
print(f'Original after reassignment:\t{list_original}')
print(f'Copy:\t\t\t\t\t\t\t{list_shallow}')
print('\n')
list_original[0] = [8,9,10]
list_original[4] = ['a', 'b']
print(f'Original:\t\t\t\t\t\t{list_original}')
list_shallow = list_original[:]
list_shallow[0][1] = 'alert'
print(f'Original after reassignment:\t{list_original}')
print(f'Copy:\t\t\t\t\t\t\t{list_shallow}')
print('\n')

print('Deep copy')
list_deep = deepcopy(list_original)
print(f'Original:\t\t\t\t\t\t{list_original}')
list_deep[0][1] = 9
print(f'Original after reassignment:\t{list_original}')
print(f'Copy:\t\t\t\t\t\t\t{list_deep}')
print('\n')



print('Custom class reassignment')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee= employee


p1 = Person('Alex', 27)
p2 = p1
p1.age = 28
print(f'Person 1 age: {p1.age}')
print(f'Person 2 age: {p2.age}')
print('Custom class shallow copy')
p2 = copy(p1)
p1.age = 20
print(f'Person 1 age: {p1.age}')
print(f'Person 2 age: {p2.age}')
print('Custom class deep copy')
company = Company(p2, p1)
company_deep = deepcopy(company)
company.boss.name = 'Horst'
print(f'Original\t\t\t\t\t\t{company.boss.name}')
print(f'Copy:\t\t\t\t\t\t\t{company_deep.boss.name}')