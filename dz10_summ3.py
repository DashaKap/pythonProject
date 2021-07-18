n = input("Введите трехзначное число: ")
n = int(n)
a = n % 10
n = n // 10
b = n % 10
n = n // 10
print("Сумма цифр числа:", n + a + b)
## Или
num = int(input("Введите число: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр числа равна: ", sum)