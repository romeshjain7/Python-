a= float(input('Enter first number'))
b= float(input('Enter second number'))
opt=int(input('Choose 1 for addition, Choose 2 for subtration, Choose 3 for multiple, Choose 4 for divide:'))
if opt==1:
    print(a+b)
elif opt==2:
    print(a-b)
elif opt==3:
    print(a*b)
elif opt==4:
    print(a/b)
else:
    print('Invalid input')