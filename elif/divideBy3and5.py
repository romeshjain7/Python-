inp=int(input('Enter a number'))
if inp%3==0 and inp%5==0:
    print(f'{inp} is divisible by 3 and 5')
    print('You are very hot ans sweet')
elif inp%5==0:
    print(f'{inp} is divisible by 5')
    print('You are very Sweet')
elif inp%3==0:
    print(f'{inp} is divisible by 3')
    print('You are very Hot')
else:
    print(f'{inp} is not divisible by 3 and 5')
    print('You are a idiot')