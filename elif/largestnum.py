a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
d=int(input("Enter fourth number"))
if a==b or b==c or a==d or a==c or b==d or c==d:
    print('any numbers are equal')
elif(a>b>c>d):
    print(f'{a} is larger')
elif(b>c>d):
    print(f'{b} is larger')
elif(c>d):
    print(f'{c} is larger')
else:
    print(f'{d} is larger')