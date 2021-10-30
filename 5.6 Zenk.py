first = int(input('Сколько в первой кучке: '))
second = int(input('Сколько во второй кучке: '))
third = int(input('Сколько в третьей кучке: '))

while first != 0 or second != 0 or third != 0:
    n = int(input())
    c = int(input())

    if n == 1:
        first -= c
        print(first, second, third)
    elif n == 2:
        first -= c
        print(first, second, third)
    elif n == 3:
        third -= c
        print(first, second, third)