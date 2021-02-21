from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
print('Counter')
a = 'aaaaaaaaaaaabbbbbbbbbbbbbbbbbbbcccccccdddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeee'
counter1 = Counter(a)
print(counter1)
print(counter1.most_common(3))
print('\n')

print('Named Tuple')
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt)
print(pt[1])
print(pt.x)
print('\n')

print('OrderedDict')
#Keeps the insertion order, less important since python 3.7 dictioanries
# keep the insertion order of items
ordered_dict = OrderedDict(a=1,b=2,c=3,d=4)
print(ordered_dict)
print('\n')

print('Default dict')
default_dict = defaultdict(int)
default_dict['a'] = 1
default_dict['b'] = 2
print(default_dict)
print(default_dict['d']) #not existant value
print('\n')

print('Deque')
d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)
d.appendleft('a')
d.appendleft('b')
d.pop()
d.popleft()
print(d)
d.extendleft((4,5,6)) #reverse insertion order!
print(d)
d.rotate(-2)
print(d)