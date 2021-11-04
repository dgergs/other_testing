num = int(input("add a number))

while num != 1:
	print(num)
	if num == 1:
		return
	elif num % 2 == 0:
		num = num/2
	else:
		num = num*3
