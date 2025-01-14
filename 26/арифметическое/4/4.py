# В текстовом файле записан набор натуральных чисел, не превышающих 109. Гарантируется, что все числа различны. Необходимо определить, сколько в наборе таких пар чётных чисел, что их среднее арифметическое тоже присутствует в файле, и чему равно наибольшее из средних арифметических таких пар.
# Входные данные.
# Задание 26
# Первая строка входного файла содержит целое число N — общее количество чисел в наборе. Каждая из следующих N строк содержит одно число.
# В ответе запишите два целых числа: сначала количество пар, затем наибольшее среднее арифметическое.
# Пример входного файла:
# 6
# 3
# 8
# 14
# 11
# 2
# 17
# В данном случае есть две подходящие пары: 8 и 14 (среднее арифметическое 11), 14 и 2 (среднее арифметическое 8). В ответе надо записать числа 2 и 11.

with open('26.txt') as f:
    N = int(f.readline())
    chet, data = list(), set()
    for i in range(N):
        x = int(f.readline())

        data.add(x)
        if x & 1 == 0:
            chet.append(x)


res = []
for i in range(0, len(chet) - 1):
    for j in range(i + 1, len(chet)):
        sr = (chet[i] + chet[j]) // 2

        if sr in data:
            res.append(sr)


print(len(res), max(res))