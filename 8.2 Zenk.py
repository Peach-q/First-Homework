print('Введите ширину')
latitude = int(input())

print('')
height = int(input('Введите высоту'))

print('Введите символ для рисования прямоугольника')
symbol = input()

print(symbol * latitude)

for i in range(height - 2):
    print(symbol, ' ' * (latitude - 2), symbol, sep='')
    
print(symbol * latitude)