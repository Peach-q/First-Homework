print('Привет, это программа, которая поможет тебе определить чётность числа'
      '\nДля продолжения работы введи целое число!')

number = int(input())

if number % 2 == 0 and number // 2 != 0 :
      print('Вы ввели чётное число!')
else:
      print('Введённое число не является чётным!')