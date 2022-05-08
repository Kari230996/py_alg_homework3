'''
Практическое задание №5

Массивы. Кортежи. Множества. Списки.
'''

import random


n = []
for i in range(1, 21):
    random_ = random.randint(-100, 101)
    n.append(random_)

print(n)

new = []

for i in n:
    if i < 0:
        new.append(i)

max_ = new[0]
for i in new:
    if i > max_:
        max_ = i

print(f'Максимальное отрицательное число: {max_}')