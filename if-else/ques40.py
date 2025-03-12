a= eval(input('Enter a list:'))
b=type(a[0:5:1])
if b==tuple:
    print('is a tuple value of list at first position')
else:
    print(' is not a tuple value in list at first position')