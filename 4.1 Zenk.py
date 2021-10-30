print('Привет, я программа-психолог, ты можешь выговориться мне. '
      'Как только захочешь закончить - напиши "Спасибо" ')

user_message = input()
a_number_of_message = 0

while(user_message != "Спасибо"):

    user_message = input()
    a_number_of_message += 1

print(a_number_of_message + 1)


