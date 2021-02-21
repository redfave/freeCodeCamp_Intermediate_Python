import random
import secrets
import numpy as np

# random.seed(10)                     # Makes pseudorandom behavior reproducible

print('Pseudorandom')
print(random.random())  # range: 0 - 1
print(random.uniform(1, 10))  # Still floats, includes upper bound
print(random.randint(1, 10))  # Includes upper bound
print(random.randrange(1, 10))  # Excludes upper bound
print(random.normalvariate(0, 1))
print('\n')

list1 = list('ABCDEFGHIJ')
print(list1)
print(random.choice(list1))
print(random.sample(list1, 3))  # Unique sample
print(random.choices(list1, k=3))  # Non unique sample
random.shuffle(list1)  # in-place
print(list1)
print('\n')

print('Secure random')
print(secrets.randbelow(10))  # Exclusive upper bound
print(secrets.randbits(4))
print(secrets.choice(list1))
print('\n')

print('Numpy random')
# np.random.seed(10)
arr = np.random.randint(0, 10, (3, 4))
print(arr)
print('\n')
np.random.shuffle(arr)
print(arr)
