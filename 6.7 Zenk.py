print('Введите количество чисел: ')

user_number = int(input())
result = 0

for i in range(user_number):
    num = int(input(f"Введите {i+1} число:\n"))
    if i % 2 == 0:
        result += num
    else:
        result -= num
print(f"Результат = {result}")