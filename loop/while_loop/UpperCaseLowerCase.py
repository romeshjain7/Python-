a=input('Enter a string')
i=0
uc=''
lc=''
while i<len(a):
    if ('A'<=a[i]<='Z'):
        uc=uc+a[i]
        
    elif 'a'<=a[i]<='z':
        lc=lc+a[i]
    i+=1
    print(uc,lc)
