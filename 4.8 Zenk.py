print('Привет, загадай число, а я попробую его отгадать!')

flag = False
program_steps = 0
left_number = 1
right_number = 1000

while not flag:
    number = (left_number + right_number) // 2
    print(f"Это {number}?")
    user_answer = input("-> ")

    if not user_answer in ("<", ">", "="):
        print('Я не понимаю в какую сторону двигаться!')
        continue

    if user_answer == "<":
        right_number = number

    elif user_answer == ">":
        left_number = number

    else:
        flag = True
    program_steps += 1

print(f"Загаданное тобой число было отгадано за {program_steps} шагов")