'''
Практическое задание №6

Массивы. Кортежи. Множества. Списки.
'''

import random

n = []
for i in range(1, 21):
    random_ = random.randint(0, 99)
    n.append(random_)

print(n)


def maxi(arr):
    max_ = arr[0]
    for i in arr:
        if i > max_:
           max_ = i
    return max_

def mini(arr):
    min_ = arr[0]
    for i in arr:
        if i < min_:
            min_ = i
    return min_


max_index = n.index(maxi(n))
min_index = n.index(mini(n))

print(f'Максимальное число: {maxi(n)}, минимальное: {mini(n)}')

a = n[min_index+1:max_index]
b = n[max_index+1:min_index]

def sumList(arr):
   if len(arr) == 1:
        return arr[0]
   else:
        return arr[0] + sumList(arr[1:])

try:
    if len(a) == 0:
        print(b)
        print(f'Сумма между максимальным и минимальным элементами: {sumList(b)}')
    else:
        print(a)
        print(f'Сумма между максимальным и минимальным элементами: {sumList(a)}')

except IndexError:
    print(None)





