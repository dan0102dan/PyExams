# Решите уравнение:
 
# 60_8 + x = 200_5.
 
# Ответ запишите в шестеричной системе (основание системы счисления в ответе писать не нужно).

X = 0
while True:
	if (int('60', 8) + X == int('200', 5)):
		print(X, hex(X)[2:])
	X += 1