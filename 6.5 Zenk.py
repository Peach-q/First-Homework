numerator, denumerator = 0, 1
for i in range(int(input("Введите количесвто дробинок\n"))):
    a = int(input("Введите урон дробинки\n"))
    b = int(input("Введите урон дробинки\n"))
    numerator = numerator * b + a * denumerator
    denumerator *= b
x, y = numerator, denumerator
while y > 0:
    x, y = y, x % y
print(numerator // x, '/', denumerator // x, sep='')