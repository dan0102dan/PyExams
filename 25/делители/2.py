# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [245 690; 245 756] простые числа. Выведите на экран все найденные простые числа в порядке возрастания, слева от каждого числа выведите его порядковый номер в последовательности. Каждая пара чисел должна быть выведена в отдельной строке.
# Например, в диапазоне [5; 9] ровно два различных натуральных простых числа  — это числа 5 и 7, поэтому для этого диапазона вывод на экране должна содержать следующие значения:
# 1 5
# 3 7
 
# Примечание. Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя.

def findDivs(num):
	divs = []

	for x in range(1, num + 1):
		if (num % x == 0):
			divs.append(x)

	return divs

allDivs = []
for i in range(245690, 245756 + 1):
	div = findDivs(i)
	if (len(div) == 2):
		allDivs.append([range(245690, 245756 + 1).index(i) + 1, i])

for div in allDivs:
	print(div)