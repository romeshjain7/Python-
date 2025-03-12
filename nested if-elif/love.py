import random
a=input('Enter first name')
b=input('Enter second name')
c=random.randint(1,100)
if c>=90:
    print(f'{a} and {b} love is strong and can marry')
elif 70<=c<=89:
    print(f'{a} and {b} can continue for love for some for more time')
elif 50<=c<=69:
    print(f'{a} and {b} love is 50-50')
elif 35<=c<=49:
    print(f'{a} and {b} love will not work being ')
else:
    print(f'{a} and {b} stay single')