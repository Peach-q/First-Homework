first_price = int(input())
second_price = int(input())
third_price = int(input())

alert_flag = False
work_flag = False


while (work_flag == False) and (third_price != 0):

    if alert_flag == False:
        if first_price > second_price and third_price > second_price:
            inprice = third_price
            alert_flag = True

    if alert_flag == True:
        if second_price > first_price  and second_price > third_price:
            outprice = third_price
            work_flag = True

    first_price = second_price
    second_price = third_price

    third_price = int(input())

print(inprice, outprice, outprice - inprice)