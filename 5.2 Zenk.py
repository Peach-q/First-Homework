result = int(input("Введите количество камней в куче: \n"))
calc = 1
a_number_of_step = 0

while not calc >= result:
    if calc * 2 < result:
        calc *= 2
    else:
        calc += 1
    a_number_of_step += 1

print(f"Потребовалось шагов: {a_number_of_step}")