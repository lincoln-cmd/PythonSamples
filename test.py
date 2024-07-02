import os
import random

print(random.random())
print(random.uniform(3, 5))

print('------------------------------')

for i in range(3):
    print(random.gauss(1, 1.0))

print('------------------------------')

print(random.randrange(20))

print([random.randrange(20) for i in range(10)])

print(random.sample(range(20), 15))
l = [random.randrange(0, 20, 2) for i in range(5)]
print(l)

print('------------------------------')

random.shuffle(l)
print(l)

print('------------------------------')