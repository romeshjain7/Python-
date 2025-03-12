int=int(input('Enter a number:'))

if (int%10)%3==0:
    print('it is divided by 3')
else:
    print('it is not divided by 3')

int=input('Enter second trick') #if we take input as a string
if int[-1] in '3690':
    print('it is divible ny 3')
else:
    print('it is not divible by 3')