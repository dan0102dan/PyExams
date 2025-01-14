"""
В городе M расположена кольцевая автодорога длиной в N километров с движением в обе стороны. 
На каждом километре автодороги расположены пункты приема мусора определенной вместимости. В пределах кольцевой дороги в одном из пунктов сборки мусора собираются поставить мусороперерабатывающий завод таким образом, чтобы стоимость доставки мусора была минимальной. Стоимость доставки мусора вычисляется как вместимость пункта сбора, умноженная на расстояние от пункта сбора мусора до мусороперерабатывающего завода. 
Если мусороперерабатывающий завод находится рядом с пунктом сбора, расстояние считается нулевым. Пункты сбора мусора нумеруются с 1 до N. Рядом с каким пунктом сбора мусора нужно поставить мусороперерабатывающий завод?
Входные данные: Даны два входных файла: файл A (27a.txt) и файл B (27b.txt), каждый из которых содержит в первой строке натуральное число N – количество контейнеров для мусора (100 ≤ N ≤ 5000000). В каждой из следующих N строк записано одно целое число в диапазоне от 1 до 1000 – количество килограммов мусора, которое производится на одном пункте приёма мусора.
Пример входного файла:
6
8
20
5
13
7
19
Для данного примера ответ — 6 (минимальная стоимость доставки мусора 7·1 + 13·2 + 5·3 + 20·2 + 8·1 + 19·0 = 96).
В ответе укажите два числа: сначала искомый номер контейнера для файла А, затем для файла B.
"""

with open("27.txt") as f:
	N = int(f.readline())
	data = list(int(f.readline()) for i in range(N))

baki = {1: 0}
# считаем, сколько будет стоит вывоз мусора из 1 бака
for i in range(N):
	baki[1] += data[i] * min(i, N - i) # берём элемент из круга и умножаем на минимальное расстояние до него
# мысленно делим круговую дорогу на две половинки и считаем их суммы
M = N // 2
left = sum(data[M:])
right = sum(data[1:M])

for i in range(1, N):
	left += data[i - 1] - data[M] # добавляем предыдущее значение и убираем середину
	right += data[M] - data[i] # добавляем середину и убираем текущее

	n = i + 1 # номер бака
	baki[n] = baki[n - 1] - data[i] + left - right # из предыдущего значения бака убираем текущую вместимость прибавляем левую и вычитаем правую части

	M = (M + 1) % N # смещаем индекс половины на единицу

print(sorted(baki.items(), key=lambda x: x[1])[0][0])