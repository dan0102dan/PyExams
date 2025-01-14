# Исполнитель преобразует число на экране. У исполнителя есть две команды, которым присвоены номера:
# 1. Удвоить
# 2. Удвоить и прибавить
# Первая команда умножает число на экране на 2, вторая — умножает его на 2, а затем прибавляет 1.
# Программа для исполнителя — это последовательность команд. Например, программа 121 при исходном числе 3 последовательно получит числа 6, 13 и 26. Результатом программы будет число 26.
# Сколько различных результатов можно получить из исходного числа 1 после выполнения программы, содержащей ровно 10 команд?

res = set()
def f(n, k):
    if k == 10:
        res.add(n)
    elif k < 10:
        return f(n * 2, k + 1) or f(n * 2 + 1, k + 1)
        
f(1, 0)
print(len(res))