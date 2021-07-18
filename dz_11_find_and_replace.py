import random
list = [random.randint(0,20) for i in range(10)]
print(list)
a=list.index(int(input("Введите значение числа из списка:")))
b=int(input("Введите число на которое необходимо заменить:"))
list[a]=(b)
print(list)
