print('Введите количество звездочек')

point = int(input())

for i in range(point):
    print(' ' * (point-i-1), '*' * (i*2+1))