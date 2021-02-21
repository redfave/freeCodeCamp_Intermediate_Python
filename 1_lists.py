list1 = ['banana', 'cherry']
list2 = list()
list2.append(5)
list2.append(True)
list2.append('apple')
list2.insert(1,'banana')
print(list2)

print(list2[1])
print(list1[-1])

def find_item(item):
    if item in list1:
        print('found {:1}'.format(item))
    else:
        print('no {a:} here'.format(a=item))

find_item('banana')
find_item('foo')

print(len(list2))

list2.remove('banana')
print(list2)
list2.reverse()
print(list2)

#inplace: list2.sort()
sorted_list = sorted(list1)  #'<' not supported between instances of 'bool' and 'str'

list3 = [1]*7 + [3]*4
print(list3)

list4 = [1,2,3,4,5,6,7,8,9]
print(list4[2:5])
print(list4[:5])
print(list4[2:])
print(list4[::2])
print(list4[::-1]) #reverse
print(list4[::-2])

#copy: foo = list2.copy() or foo = list(list2) or foo = list2[:]

list5 = [i**2 for i in list4]
print(list5)