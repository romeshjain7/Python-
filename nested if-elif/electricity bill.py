a=int(input('enter unit'))
total_bill=0
if 0<=a<=100:
    print('bill is free')
elif 101<=a<=200:
    print(f'your bill is,{(a-100)*5}')
    total_bill=(a-100)*5
elif 201<=a<=300:
    total_bill=(a-100)*5
    print(total_bill)
    print(f'your bill is,{((a-200)*5)+total_bill}')
    print((a-200)*5)
else:
    print('directly your bill is 2000')
