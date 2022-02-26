# В текстовом файле записан набор натуральных чисел, не превышающих 109. Гарантируется, что все числа различны. Необходимо определить, сколько в наборе таких пар чисел, что числа в паре имеют разную чётность, а их сумма тоже присутствует в файле, и чему равна наибольшая из сумм таких пар.
# Входные данные.
# Задание 26
# Первая строка входного файла содержит целое число N — общее количество чисел в наборе. Каждая из следующих N строк содержит одно число.
# В ответе запишите два целых числа: сначала количество пар, затем наибольшую сумму.
# Пример входного файла:
# 6
# 3
# 8
# 14
# 11
# 22
# 17
# В данном случае есть две подходящие пары: 3 и 8 (сумма 11), 3 и 14 (сумма 17). В ответе надо записать числа 2 и 17.

with open('inf_26_04_21_26.txt') as f:
	N = int(f.readline())
	count, maxsumma = 0, 0

	arr = [int(f.readline()) for i in range(N)]
	setArr = set(arr) # тут быстрее происходит поиск

	for i in range(len(arr) - 1):
		for j in range(i + 1, len(arr)):
			if arr[i] & 1 != arr[j] & 1:
				summa = arr[i] + arr[j]
				if summa in setArr:
					count += 1
					maxsumma = max(summa, maxsumma)
	print(count, maxsumma)