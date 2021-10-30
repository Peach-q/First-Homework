print('Введите свой пароль: ')

user_password = input()

if len(user_password) < 8:
    print("Ваш пароль короче 8 символов!")

elif "123" in user_password:
    print("Пароль простой")
else:
    user_password2 = input("Введие пароль еще раз: \n")

    if user_password != user_password2:
        print("Ваши пароли различаются!")
    else:
        print("OK")