a=eval(input('Enter a value'))
if type(a)==int:
    if 10<=a<=99:
        print(f'{a%10}{a//10}')
    else:
        print(a**2)
else:
    print(f'{a} is not a integer')
