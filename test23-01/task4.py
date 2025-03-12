a=int(input('Enter first cieffifents'))
b=int(input('Enter first cieffifents'))
c=int(input('Enter first cieffifents'))
x=(b**2)-(4*a*c)
qe=a*(x**2)+(b*x)+c
if (qe<0):
    print('Real and distinct')
elif (qe==0):
    print('Real and equal')
else:
    print('complex')