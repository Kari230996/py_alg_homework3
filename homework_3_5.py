'''
Практическое задание №5

Массивы. Кортежи. Множества. Списки.
'''

import random

def maxi(arr):
    max_ = arr[0]
    for i in arr:
        if i > max_:
           max_ = i
    return max_


n = []
for i in range(1, 21):
    random_ = random.randint(-100, 101)
    n.append(random_)

print(n)

new = []

for i in n:
    if i < 0:
        new.append(i)

print(new)
print(f'Максимальное отрицательное число: {maxi(new)}')