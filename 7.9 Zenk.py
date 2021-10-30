c = ''
f = 1
while c != 'x':
    a = int(input("Введите первое число\n"))
    c = input("Введите действие\n")
    if c == 'x':
        print(a)
        break
    else:
        if c == '+':
            b = int(input("Введите второе число\n"))
            print(a + b)
        elif c == '-':
            b = int(input("Введите второе число\n"))
            print(a - b)
        elif c == '*':
            b = int(input("Введите второе число\n"))
            print(a * b)
        elif c == '/':
            b = int(input("Введите второе число\n"))
            if b == 0:
                continue
            else:
                print(a // b)
        elif c == '!' and a > 0:
            for i in range(1, a + 1):
                f *= i
            print(f)
        elif c == '%':
            b = int(input("Введите второе число\n"))
            if b == 0:
                continue
            else:
                print(a % b)