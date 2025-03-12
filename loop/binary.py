a=input('Enter a binary no.')
length=len(a)
i=0
sum=0
while length>0:
    result=(int(a[length-1])*(2**i))
    sum=sum+result
    length-=1
    i+=1
print(sum)  