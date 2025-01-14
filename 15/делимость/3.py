# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наименьшего натурального числа А формула
# (ДЕЛ(x, 3) → ¬ДЕЛ(x, 5)) ∨ (x + A ≥ 90)
# тождественно истинна (т. е. принимает значение 1) при любом натуральном значении переменной x?

def d(n, m):
    return n % m == 0
def f(A):
    for x in range(1, 10*6):
        if not(((d(x, 3)) <= (not(d(x, 5)))) or (x + A >= 90)):
            return False
    return True

A = 1
while not(f(A)):
    A += 1
print(A)