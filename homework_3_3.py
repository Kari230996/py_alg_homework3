'''
Практическое задание №3

Массивы. Кортежи. Множества. Списки.
'''

import random
SIZE = 10

n = []

for i in range(SIZE):
    random_ = random.randint(0, 99)
    n.append(random_)

print(n)

max_ = 0
min_ = 0

for i in range(len(n)):
    if n[i] > n[max_]:
        max_ = i
    elif n[i] < n[min_]:
        min_ = i

print(f'Максимальное число: {n[max_]}, минимальное: {n[min_]}')

n[max_], n[min_] = n[min_], n[max_]

print(n)


