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

max_index = 0
min_index = 0

for i in range(len(n)):
    if n[i] > n[max_index]:
        max_index = i
    elif n[i] < n[min_index]:
        min_index = i



print(f'Максимальное число: {n[max_index]}, минимальное: {n[min_index]}')

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





