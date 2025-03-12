a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
if a==b:
    print(f'{a} is equal to {b}')
elif a>b:
    print(f'{a} is greater then {b}')
elif a<b:
    print(f'{b} is greater then {a}')
elif a!=b:
    print(f'{a} is not equal to {b}')
else:
    print('Wrong input')