symbols = set("Hello")
print(symbols)
print(len(symbols))

set1 = {1, 2, 3, 3, 3, 4}
print(set1)

set1.add(7)
set1.discard(3)  # unsafe call: set1.remove(3)
print(set1)

odds = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setC = {1,2,3}

print('Union: ', odds | even)
print('Intersection: ', odds & primes)
print('Difference A - B: ', setA - setB)
print('Difference B - A: ', setB - setA)
print('union without Intersection: ', odds ^ primes)

print(setC < setA)

#there are frozensets
forezenSet = frozenset((1,2,3,4))
print(forezenSet)