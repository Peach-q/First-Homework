print('Привет, я небольшая чат-программа, давай немного пообщаемся :) Как твои дела?')

user_answer = str(input())
user_answer = user_answer.lower()

if 'хорош' in user_answer:
    print('Стабильность тоже неплохо!')
elif 'отличн' in user_answer:
    print('Отлично, у меня тоже всё хорошо :)')
elif 'прекрас' in user_answer:
    print('У меня тоже всё хорошо :)')
elif 'плох' in user_answer:
    print('Всё придёт в норму, только приложи усиия')
elif 'отврат' in user_answer:
    print('Тяжёлые времена иногда наступают, главное их пережить.')
else:
    print('Ой! Мне пора! Спасибо за разговор.')