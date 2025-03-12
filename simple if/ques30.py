a=eval(input("enter a value:"))
if type(a) not in [int,float,complex,bool,str,tuple]:
    print(f'{a} is mutable')
