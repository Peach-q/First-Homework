print('Введите количество человек: ')
testing_human = int(input())

print('Введите IQ человека: ')
iq = int(input())

print(0)

for n in range(1, testing_human):

    iq_for_prog = int(input())

    if iq_for_prog > iq:
        print('>')

    elif iq_for_prog < iq:
        print('<')

    else:
        print(0)
    iq = (iq * n + iq_for_prog) / (n + 1)