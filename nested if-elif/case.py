a=int(input('Enter a number or character'))
if len(a)!=1:
    print('invalid input,please enter one digit character only')
else:
    if 'a'<=a<='z'or 'A'<=a<='Z':
        if 'A'<=a<='Z':
            print(f'{a} is upper case')
        else:
            print(f'{a} is lower case')

    elif '0'<=a<='9':
        print(f'{a} is digit')
    else:
        print('special ')


