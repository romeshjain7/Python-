a=int(input('enter the age of a'))
b=int(input('enter the age of b'))
if a>b:
    print(f'{a} is elder then {b}')
else:
    print(f'{b} is elder then {a}')

n1=eval(input('enter your name and age')) #this will print the name of the person
n2=eval(input('enter your name and age'))
if n1[1]>n2[1]:
    print(f'{n1[0]} is elder than {n2[0]}')
else:
    print(f'{n2[0]} is elder than {n1[0]}')