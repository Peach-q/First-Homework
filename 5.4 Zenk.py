import random
alert_flag = False

print('Привет, давай сыграем с тобой в ним?'
      '\nПравила такие: на нас двоих одна куча камней, нельзя брать за раз больше трёх!'
      '\nВыирывает тот, кто возьмёт последним из кучи все камни!')

print('Задай количетсво камней в куче: ')
a_number_of_rock = input()

while not alert_flag:

      print('Ты задал количество камней, их ' + str(a_number_of_rock) + ' в куче. Я делаю свой ход.')
      program_number = random.randint(1, 3)
      a_number_of_rock = int(a_number_of_rock) - program_number

      while a_number_of_rock < 0:
            program_number = 1
            a_number_of_rock = int(a_number_of_rock) - program_number
      if a_number_of_rock == 0:
                print('Сейчас 0 камней в куче!')
                print('Я победила!')

      if a_number_of_rock > 0:
            print('Сейчас в куче ' + str(a_number_of_rock) + ' камней. Твоя очередь взять из кучи камни.')

      user_number = int(input())
      a_number_of_rock = a_number_of_rock - user_number

      if a_number_of_rock == 0:
            alert_flag = False
            print('Сейчас 0 камней в куче!')
            print('Игра окончена! Ты победил!')
            break