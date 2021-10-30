print('Привет, это программа, которая поможет впечатлить Машу'
      '\nВведи трёхзначное число: ')

first_number, second_number, third_number = input()

first_number = int(first_number)
second_number = int(second_number)
third_number = int(third_number)

if first_number < second_number < third_number and (first_number + third_number) / 2 == second_number:
    print('Вы ввели красивое число!')
else:
    print('Вы ввели обычное число!')