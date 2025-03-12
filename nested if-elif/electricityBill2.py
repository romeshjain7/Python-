a=int(input('enter unit'))
total_bill=0
if 0<=a<=100:
    total_bill=a*5
    print(f'bill is {total_bill}')
total_bill=a*5

elif 101<=a<=200:
    a=a-100
    total_bill=total_bill+(a*7)
    print(f'your bill is,{total_bill}')
total_bill=total_bill+(a*7)
else:
total_bill=total_bill+(a*7)

    a=a-200
    total_bill=(total_bill+(a*10))+10/100
    print(f'your bill is,{total_bill}')
