# Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки цифр.
#   заменить (v, w)
#   нашлось (v)
# Дана программа для исполнителя Редактор:
#   НАЧАЛО
#   ПОКА нашлось (222) ИЛИ нашлось (888)
#     ПОКА нашлось (555)
#       заменить (555, 8)
#     КОНЕЦ ПОКА
#     ЕСЛИ нашлось (222)
#       ТО заменить (222, 8)
#       ИНАЧЕ заменить (888, 2)
#     КОНЕЦ ЕСЛИ
#   КОНЕЦ ПОКА
#   КОНЕЦ
# Дана строка, состоящая из 21 цифры, причем первые три цифры — двойки, а остальные — пятерки. Какая строка получится в результате применения программы к данной строке?

str = ('2' * 3) + ('5' * 18)
while ('222' in str) or ('888' in str):
	while ('555' in str):
		str = str.replace('555', '8', 1)
	if '222' in str:
		str = str.replace('222', '8', 1)
	else:
		str = str.replace('888', '2', 1)
print(str)