
numbers = [5,7,1,2,9,8,10,3,6,4]
print(numbers)
a = int(input("Введите число из списка: "))
b = numbers.index(a)
print("число " + str(a) + " находится в списке под номером " + str(b))