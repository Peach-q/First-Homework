print('Введите количество строк: ')

string = int(input())

for i in range(string):
    word = input("Введите фразу\n")
    
    if "Кот" in word or "кот" in word or "Кошка" in word or "кошка" in word:
        print("МЯУ")
    else:
        print("НЕТ")