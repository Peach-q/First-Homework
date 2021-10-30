print('Введи нексолько чисел: ')

user_chislo = int(input())

while user_chislo % 10 == 0:
    user_chislo = int(input())
else:
    print(' ')