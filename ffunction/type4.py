def ar_op(a,b,op):
    if op=='+':
        res=a+b
    elif op=='-':
        res=a-b
    elif op=='*':
        res=a*b
    elif op=='/':
        res=a/b
    else:
        res=("invalid")
    return res
        
print(ar_op(int(input("Enter first Number")),int(input('Enter second number:')),input("Enter a operation")))
