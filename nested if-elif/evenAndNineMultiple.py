a=int(input('Enter a number'))
if a%2==0:
    if a%9==0:
        print(f'{a} is even and multiple of 9')
    else:
        print(f'{a} is even but not a multiple of 9')
else:
    print(f'{a} is odd number')