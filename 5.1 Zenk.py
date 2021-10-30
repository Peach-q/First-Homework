d = int(input("Введи день рождения: \n"))
m = int(input("Введи месяц рождения: \n"))
y = int(input("Введи год рождения: \n"))

calc = int( y / 100)
current = (( y - calc) % 100)

formula = d + ((13 * m - 1) // 5) + current + (current // 4 + calc // 4 - 2 * calc + 777)
formula  %= 7

print(' ')
print(formula)