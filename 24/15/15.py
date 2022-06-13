# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
# Например, в тексте CBCABABACCC есть комбинации CBC, ABA (два раза), BAB и CCC. Чаще всего — 3 раза — между двумя одинаковыми символами стоит B, в ответе для этого случая надо написать B.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

with open('24.txt') as f:
	s = f.readline().strip()

	letters = {}
	for i in range(1, len(s) - 1):
		if s[i - 1] == s[i + 1]:
			if s[i] not in letters:
				letters[s[i]] = 1
			else:
				letters[s[i]] += 1

	print(
		sorted(letters.items(), reverse=True, key=lambda x: x[1])[0][0]
	)			