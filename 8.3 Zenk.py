print('Введите размер субсидии')
credit = int(input())

print('Введите количество голов скота')
heds_skot = int(input())

for i in range(1, credit // 20 + 1):

    for j in range((credit - i * 20) // 10 + 1):
        res = heds_skot - i - j

        if i * 20 + j * 10 + res * 5 == credit:
            
            print(i, j, res)