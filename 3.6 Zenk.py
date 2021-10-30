print('Привет, это программа, которая поможет определить надежность кода для сейфа'
      '\nВведи трёхзначное число: ')

first_number, second_number, third_number = input()

first_number = int(first_number)
second_number = int(second_number)
third_number = int(third_number)


if first_number == second_number == third_number :
    print('В коде три одинаковых числа')
elif first_number == second_number or first_number == third_number or second_number == third_number :
    print('В коде два одинаковых числа')
elif first_number != second_number and first_number != second_number and second_number != third_number :
    print('ОК')