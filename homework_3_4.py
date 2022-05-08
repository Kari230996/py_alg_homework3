'''
Практическое задание №4

Массивы. Кортежи. Множества. Списки.
'''

import random

n = []

for i in range(1, 101):
    random_ = random.randint(0, 99)
    n.append(random_)
print(n)

maxi = n[0]
max_count = n.count(maxi)

for i in n:
    if n.count(i) > max_count:
        maxi = i
        max_count = n.count(i)


print('Число', maxi, 'встречается', max_count, 'раз(а)')




