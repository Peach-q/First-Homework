print('Привет, введи два дробных числа, а затем математическое действие, которое ты хочешь произвести над этими числами! ')
print('Если ты увидишь 888888, то это значит, что ты ввёёл данные с ошибкой или же что-то забыл ввести!')

first_chislo = float(input())
second_chislo = float(input())
third_znak = str(input())

if third_znak == '+' :
    print(first_chislo + second_chislo)
elif third_znak == '-' :
    print(first_chislo - second_chislo)
elif third_znak == '/' :
    print(first_chislo / second_chislo)
elif third_znak == '*' :
    print(first_chislo * second_chislo)
else:
    print('888888')