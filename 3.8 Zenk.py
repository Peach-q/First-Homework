print('Привет, эта программа поможет зашифровать число.'
      '\nВведи число: ')

first_number, second_number, third_number = input()

first_number = int(first_number)
second_number = int(second_number)
third_number = int(third_number)

first_sum = first_number + second_number
second_sum = second_number + third_number

if first_sum > second_sum:
    print( first_sum, second_sum)
else:
    print(second_sum, first_sum)