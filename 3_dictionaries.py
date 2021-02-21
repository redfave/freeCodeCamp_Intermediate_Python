dict1 = {'name': 'Max', 'age': 28, 'city': 'New York'}
print(dict1)
dict2 = dict(name='Mary', age=27, city='Boston')
print(dict2)
print(dict2['name'])

#add pair
dict1['email'] = 'max@xyz.com'
print(dict1)
#override existing pair
dict1['email'] = 'max@aol.com'
print(dict1)

del dict1['email']
print(dict1)

#access values 1
if 'name' in dict1:
    print(dict2['name'])

#access values 2
try:
    print(dict1['foo'])
except:
    print('dict has no foo key')


for key in dict1.keys():
    print(key)
for value in dict1.values():
       print(value)
for key, value in dict1.items():
    print(f'{key}: {value}')

#merge
dict3 = {'a': 1, 'b': 2, 'c': 3}
dict4 = {'a': 4, 'b': 5, 'd': 6}
dict3.update(dict4)
print(dict3)

dict5 = {3: 9, 6: 36, 9: 81}
print(dict5[9]) #no index access with numebrs

