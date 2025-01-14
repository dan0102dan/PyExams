# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [174457; 174505], числа, имеющие ровно два различных натуральных делителя, не считая единицы и самого числа. Для каждого найденного числа запишите эти два делителя в два соседних столбца на экране с новой строки в порядке возрастания произведения этих двух делителей. Делители в строке также должны следовать в порядке возрастания.
# Например, в диапазоне [5; 9] ровно два различных натуральных делителя имеют числа 6 и 8, поэтому для этого диапазона вывод на экране должна содержать следующие значения:
# 2 3
# 2 4

def findDel(num):
	result = []
	for d in range(2, num):
		if num % d == 0:
			result.append(d)
	return result

results = []
for x in range(174457, 174505 + 1):
	res = findDel(x)
	if len(res) == 2:
		results.append(res)
	
print(sorted(results, key=lambda x: x[0] * x[1]))

# вывод в столбик
for arr in sorted(results, key=lambda x: x[0] * x[1]):
	print(arr)