# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z). Определите количество строк, в которых буква E встречается чаще, чем буква A.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

with open('inf_22_10_20_24.txt') as f:
	s = list(map(lambda x: x.strip(), f.readlines()))
	res = 0

	for line in s:
		if line.count('E') > line.count('A'):
			res += 1
	
	print(res)