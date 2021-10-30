print('Привет! Это твой личностный тест, пожалуйста, ответь на несколько вопросов!')

system_answer_1 = 'балет'
system_answer_2 = 'уличные танцы'
system_answer_3 = 'танго'

system_answer_1_1 = 'чёрный'
system_answer_1_2 = 'белый'
system_answer_1_3 = 'серый'

system_answer_2_1 = 'коты'
system_answer_2_2 = 'собаки'
system_answer_2_3 = 'птицы'

print('\nПервый вопрос!'
      '\nКакой стиль танца ты предпочитаешь больше всего? Введи название стиля!'
      '\n *Балет'
      '\n *Уличные танцы'
      '\n *Танго')

user_answer = input()
user_answer = user_answer.strip()
user_answer = user_answer.lower()

if user_answer == system_answer_1:
    print('Зачастую балет предпочитают люди, которые являются тонкими душевными натурами.')
elif user_answer == system_answer_2:
    print('Вам не хватает динамики в буднях, раскрасьте свои скучные дни!')
elif user_answer == system_answer_3:
    print('Танго больше подходит страстным людям, задумайтесь, может быть, Вы страстный романтик?')
else:
    print('Такого варианта нет, о Вас нечего сказать!')


print('\nВторой вопрос!'
      '\nКакой цвет в гардеробе преобладает? Введи название!'
      '\n *Чёрный'
      '\n *Белый'
      '\n *Серый')

user_answer = input()
user_answer = user_answer.strip()
user_answer = user_answer.lower()

if user_answer == system_answer_1_1:
    print('Ты предпочитаешь строгий стиль в одежде и в любой компании ты выделяешься за счёт присущей только тебе суровости.')
elif user_answer == system_answer_1_2:
    print('Ты лёгкий на подъём человек и ты согласен воплотить многие идеи!')
elif user_answer == system_answer_1_3:
    print('Ты очень спокойный и не агрессивный человек, но как только понадобится поставить кого-то на место - ты непременно сделаешь это!')
else:
    print('Такого варианта нет, о Вас нечего сказать!')

print('\nТретий вопрос!'
      '\nКакие у тебя самые любимые животные? Введи название!'
      '\n *Коты'
      '\n *Собаки'
      '\n *Птицы')

user_answer = input()
user_answer = user_answer.strip()
user_answer = user_answer.lower()

if user_answer == system_answer_2_1:
    print('Ты азартный человек и предпочитаешь брать на слабо других людей.')
elif user_answer == system_answer_2_2:
    print('Ты верен тому, к кому привязываешься, и следуешь за ним до конца.')
elif user_answer == system_answer_2_3:
    print('Ты мечтательный человек и витаешь в облаках!')
else:
    print('Такого варианта нет, о Вас нечего сказать!')
