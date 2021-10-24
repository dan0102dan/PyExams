# Для какого наименьшего целого числа А формула
#   ((x < 11) → (x⋅x < A)) ∧ ((y⋅y < A) → (y ≤ 12))
# тождественно истинна (то есть принимает значение 1 при любых целых неотрицательных значениях переменных x и y)?

def checker(A):
	for x in range(10000):
		for y in range(10000):
			if not(((x < 11) <= (x*x < A)) and ((y*y < A) <= (y <= 12))):
				return False
	return True

A = -100000

while True:
	if checker(A):
		print(A)
	A += 1