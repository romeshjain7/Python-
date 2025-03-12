a=int(input('Enter first number'))
b=int(input('Enter second number'))
if (a>b):
    c=a-b
else:
    c=b-a   
if(c%2==0 and c>10):
    print(f' difference is even and greater then 10 and diffference is {c}')
elif(c%2!=0 and c>15):
    print(f'difference is odd and greater then 15 and difference is {c}')
else:
    print(f'{c}')