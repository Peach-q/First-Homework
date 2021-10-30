print('Введите запас терпения: ')

user_answer = int(input())
currect = 0

while user_answer:
    for counting in ("раз", "два", "три", "четыре"):
        if counting == input():
            currect += 1
        else:
            print(f"Правильных отсчётов было {currect}, но теперь вы ошиблись")
            currect -= 1
            user_answer -= 1
            break

print("На сегодня хватит")