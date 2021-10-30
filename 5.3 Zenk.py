print('Это игра Ним2-пасьянс')

first = int(input("Сколько камней в первой кучке: "))
second = int(input("Сколько камней во второй кучке: "))

while first != 0 or second != 0:

    which = int(input("Из какой кучки брать камни: ")) - 1
    how_many = int(input("Сколько камне надо взять: "))

    if which:
        second -= how_many
        print(first, second)
    else:
        first -= how_many
        print(first, second)

