inp=int(input('Enter a number:'))
if inp%2!=0:
    if inp%3==0 and inp%5==0  and inp%7==0:
        print(f'{inp} is multiple of first three odd number')
    else:
        print(f'{inp} is not a multiple of first three odd number')
else:
    print(f'{inp} is even number')

