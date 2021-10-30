print('Введите количество секунд: ')

sec = int(input())
alert_flag = False

while not alert_flag:

    if sec > 0:
        sec -= 1
        print('Осталось секунд: ' + str(sec) )

    if sec == 0:
        print('Пуск')
        alert_flag = True

    if sec < 0 :
        alert_flag = True
        print('Пуск')