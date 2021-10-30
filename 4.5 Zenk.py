print('Введите число, а я определю, сколько шагов потребуется для того, чтобы получить 1, благодаря сиракузской последовательности')

user_chislo = int(input())
my_counter = 0

while user_chislo != 1:

    if user_chislo % 2 == 0:
        user_chislo = user_chislo // 2
        my_counter += 1
    else:
        user_chislo = 3 * user_chislo + 1
        my_counter += 1

print(my_counter)


