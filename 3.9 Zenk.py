print('Привет! Я - программа, которая поможет тебе рассчитать стоимость телеграммы.'
      '\nВведи своё сообщение: ')

user_letter = str(input())
user_letter = len(user_letter)

len_user_letter = int(user_letter)

symbols = len_user_letter * 40
rub_symbols = symbols // 100
kop_symbols = symbols % 100

rub_symbols = str(rub_symbols)
kop_symbols = str(kop_symbols)

print(rub_symbols + ' р. ' + kop_symbols + ' коп. ')