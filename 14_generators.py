import sys


def my_generator():
    for i in range(11):
        yield i


g = my_generator()
print(g)

# value = next(g)
# print(value)

print(sum(sorted(g)))


def count_down(start):
    print('Starting')
    while start > 0:
        yield start
        start -= 1


cd = count_down(10)
value = next(cd)
print(value)

for i in cd:
    print(i)
print('\n')

print('Large data generation')


def first_n(n):
    nums = []
    index = 1
    while index <= n:
        nums.append(index)
        index += 1
    return nums


def first_n_generator(n):
    index = 1
    while index <= n:
        yield index
        index += 1


list = first_n(1000000)
print(sum(list))
print(sys.getsizeof(list))

generator = first_n_generator(1000000)
print(sum(generator))
print(sys.getsizeof(generator))


def fibonacci_generator(limit):
    a, b, = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


for i in fibonacci_generator(100):
    print(i)
print('\n')

print('Generator expressions')
generator = (i for i in range(11) if i % 2 == 0)
for i in generator:
    print(i)
