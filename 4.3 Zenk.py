print('Введи какое-нибудь число, а я определю, является лионо степенью двойки')

user_chislo = int(input())
counter = 0

if user_chislo == 1:
    print(0)

while user_chislo > 1:

   user_chislo = user_chislo / 2
   counter += 1

   if user_chislo == 1:
       print(counter)

   elif user_chislo < 1:
       print('НЕТ')