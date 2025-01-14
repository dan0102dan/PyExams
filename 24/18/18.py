# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.
# Например, в тексте ABCAABAKLD самая длинная цепочка символов, удовлетворяющая условию — ABCAABAK, её длина равна 8.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

with open('24.txt') as f:
	s = f.readline().strip()

	res, cur = 0, 0

	for i in range(len(s) - 1):
		if s[i:i+2] in ['KL', 'LK']:
			cur = 0
		else:
			cur += 1
		res = max(res, cur + 1)

	print(res)