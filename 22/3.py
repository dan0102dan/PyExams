# Ниже на пяти языках программирования записан алгоритм. Получив на вход число x, этот алгоритм печатает числа: a и b. Укажите наибольшее четырехзначное число x, при вводе которого алгоритм печатает сначала 5, а потом 7.

def func(x):
	a = 10
	b = 0
	# x = int(input())
	while x > 0:
		y = x % 10
		x = x // 10
		if y < a:
			a = y
		if y > b:
			b = y

	return (a, b)
	# print(a)
	# print(b)

x = 0
while True:
	if (func(x) == (5, 7) and (len(str(x)) == 4)):
		print(x)
	x += 1