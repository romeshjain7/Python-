a=145
num=0
total=0
while(a>0):
    product=1
    rem = a%10
    for i in range(1,rem+1):
        product = product*i
        total=product+total
    num=num//10
print(total)
    
    
