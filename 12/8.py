# Исполнитель Редактор получает на вход строку цифр и преобразовывает её. Редактор может выполнять две команды, в обеих командах v и w обозначают цепочки цифр.
#   заменить (v, w)
#   нашлось (v)
# Дана программа для исполнителя Редактор:
#   НАЧАЛО
#   ПОКА нашлось (333) ИЛИ нашлось (555)
#     ЕСЛИ нашлось (555)
#       ТО заменить (555, 3)
#       ИНАЧЕ заменить (333, 5)
#     КОНЕЦ ЕСЛИ
#   КОНЕЦ ПОКА
#   КОНЕЦ
# Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 193 идущих подряд цифр 5? В ответе запишите полученную строку.

str = '5' * 193
while ('333' in str) or ('555' in str):
	if ('555' in str):
		str = str.replace('555', '3', 1)
	else: 
		str = str.replace('333', '5', 1)
print(str)