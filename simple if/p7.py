str=input('Enter you name')
val=""
c=len(str)
for i in range(0,len(str)):
    print(' '*c,end=' ')
    for j in range(i+1):
        print(str[j],end=' ')
    print()
    c-=1