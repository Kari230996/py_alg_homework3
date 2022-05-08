'''
Практическое задание №1

Массивы. Кортежи. Множества. Списки.
'''


num = {}

for i in range(2, 10):
    num[i] = []

    for j in range(2, 100):
        if i % j == 0:
            num[i].append(j)

    print(f'Число {i} кратно - {num[i]}, количество кратности - {len(num[i])}')





