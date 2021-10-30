counter = 0
summ = 0
word = ""
while word != "Стоп":
    word = input("Введите предложение,  слово \"СТОП\" - останавливает выполнение программы \n")
    counter += 1
    if "Кот" in word or "кот" in word or "Кошка" in word or "кошка" in word:
        summ += 1
        print(f"Кот был уопмянут в строке: {counter} кол-во найденных котов: {summ}")
    else:
        print("-1")