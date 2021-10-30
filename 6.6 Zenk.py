import math

print('Введите натуральное число n: ')

user_number = int(input())
k = 0

for i in range(1, user_number+1):
    k = k + i**-2
print(math.pi**2/k)