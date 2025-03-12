a=eval(input('Enter first variable:'))
b=eval(input('Enter second variable:'))
if id(a)==id(b):
    print(f'{a} and {b} is having same memory location')
else:
    print(f'{a} and {b} is not having same memory location')