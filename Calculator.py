a = int(input('Введите "a"'))
b = int(input('Введите "b"'))
c = int(input('Введите "c"'))

D = b ** 2 - 4 * a * c
print ("Дискриминант равен" , D)

if D < 0:
	print("Корней здесь нет")
elif D == 0:
	x1 = -b / (a * 2)
	print ("Единственный корень", x1)
else:
	x1 = (-b + D ** 0.5 ) / (2 * a)
	x2 = (-b - D ** 0.5 ) / (2 * a)
	print ("Первый корень", x1 , "Второй корень", x2)