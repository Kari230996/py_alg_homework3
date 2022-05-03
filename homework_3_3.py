'''
Практическое задание №3

Массивы. Кортежи. Множества. Списки.
'''

import random

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

n = []
for i in range(1, 11):
    random_ = random.randint(0, 99)
    n.append(random_)


result = maxi(n)
result_ = mini(n)


def getIndex(arr):
    min_ = arr.index(mini(arr))
    max_ = arr.index(maxi(arr))
    if min_ > max_:
        return min_, max_
    return max_, min_

print(f'Максимальное число: {result}, минимальное: {result_}')

print(n)

n[getIndex(n)[0]], n[getIndex(n)[1]] = n[getIndex(n)[1]], n[getIndex(n)[0]]

print(n)



