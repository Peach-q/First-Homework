first_totalizer = 0
second_totalizer = 0

while True:
    temperature = float(input('Введи значение температуры:'))
    if temperature > 0:
        second_totalizer += 1
        first_totalizer += temperature
    elif temperature <= -300:
        break

print(first_totalizer/second_totalizer)