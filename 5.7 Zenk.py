print('Привет, это игра Ним2. Давай поиграем в неё со мной? Взявший последний камень выигрывает!'
      '\nВведи количество камней в двух кучках!'
      '\nПервая кучка: ')
first = int(input())

print('Вторая кучка: ')
second = int(input())

program_number = 1

while first != 0 or second != 0:

    print('Я делаю свой ход: ')
    first = first - program_number
    second = second - program_number
    print(first, second)

    print('Сколько ты хочешь взять из первой кучки?')
    user_choice = int(input())
    first = first - user_choice

    print('Сколько ты хочешь взять из второй кучки?')
    user_choice = int(input())
    second = second - user_choice

    if first == 0 or second == 0:
        print('Игра окончена! Ты победил!')
        break