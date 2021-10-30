print('Привет, введи два слова "да" и "нет" в разной последовательности!')

first_word = str(input())
second_word = str(input())

first_word = first_word.strip().lower()
second_word = second_word.strip().lower()

if first_word == 'да' and second_word == 'нет' :
    print('ВЕРНО')
elif first_word == 'нет' and second_word == 'да' :
    print('ВЕРНО')
elif first_word == 'да' and second_word == 'да' :
    print('ВЕРНО')
elif first_word == 'нет' and second_word == 'нет' :
    print('ВЕРНО')
else:
    print('НЕВЕРНО')