a=int(input('Enter a number'))
if a%3==0:
    if a%5==0:
        if a%7==0:
            print(f'{a} is multiple of 3,5 and 7')
        else:
            print(f'{a} is multiple of 3 and 5 but not of 7')
    else:
        print(f'{a} is multiple of 3 not of 5')
else:
    print(f'{a} is not a multiple of 3,5 and 7')
