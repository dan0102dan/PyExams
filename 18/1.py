# Квадрат разлинован на N×N клеток (1 < N < 17). Исполнитель Робот может перемещаться по клеткам, выполняя за одно перемещение одну из двух команд: вправо или вниз. По команде вправо Робот перемещается в соседнюю правую клетку, по команде вниз — в соседнюю нижнюю. При попытке выхода за границу квадрата Робот разрушается. Перед каждым запуском Робота в каждой клетке квадрата лежит монета достоинством от 1 до 100. Посетив клетку, Робот забирает монету с собой; это также относится к начальной и конечной клетке маршрута Робота.
# Задание 18
# Откройте файл. Определите максимальную и минимальную денежную сумму, которую может собрать Робот, пройдя из левой верхней клетки в правую нижнюю. В ответ запишите два числа друг за другом без разделительных знаков — сначала максимальную сумму, затем минимальную.
# Исходные данные представляют собой электронную таблицу размером N×N, каждая ячейка которой соответствует клетке квадрата.
# Пример входных данных:
 
# 1		8	8	4
# 10	1	1	3
# 1		3	12	2
# 2		3	5	6
 
# Для указанных входных данных ответом должна быть пара чисел 41 и 22.


# combinations = []

# for a in [10, 8]:
# 	for b in [1, 1, 8]:
# 		for c in [2, 3, 1, 4]:
# 			for d in [3, 12, 3]:
# 				for e in [5, 2]:
# 					for f in [6]:
# 						combinations.append(1+a+b+c+d+e+f)

# print(max(combinations), min(combinations))