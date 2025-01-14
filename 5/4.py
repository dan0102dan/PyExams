# Автомат обрабатывает натуральное число N (0 ≤ N ≤ 255) по следующему алгоритму:
# 1.  Строится восьмибитная двоичная запись числа N.
# 2.  Все цифры двоичной записи заменяются на противоположные (0 на 1, 1 на 0).
# 3.  Полученное число переводится в десятичную запись.
# 4.  Из нового числа вычитается исходное, полученная разность выводится на экран.
# Пример. Дано число N = 13. Алгоритм работает следующим образом.
# 1.  Восьмибитная двоичная запись числа N: 00001101.
# 2.  Все цифры заменяются на противоположные, новая запись 11110010.
# 3.  Десятичное значение полученного числа 242.
# 4.  На экран выводится число 242 − 13 = 229.

# Какое число нужно ввести в автомат, чтобы в результате получилось 111?

def f(N):
    R = bin(N)[2:].zfill(8) # 1.
    R = ''.join(map(lambda x: '0' if x == '1' else '1', R)) # R.replace('1', '-').replace('0', '1').replace('-', '0')
    R = int(R, 2) # 3.
    return R - N # 4.

for N in range(0, 255 + 1):
    if f(N) == 111:
        print(N)