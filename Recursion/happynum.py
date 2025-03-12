# a=19
# num=0
# total=0
# def happy(a):
#     while(a>0):
#         product=1
#         sq=0
#         rem=a%10
#         sq=rem**2
#         a=a//10
#         total=total+sq
#     happy(a)
# happy(a)

    
#     if total ==1:

#         return(total)
#     else:
#         print('not a happy number')

def happy(a,out=0):
    global temp
    temp=0
    for i in a:
        out+=int(i)**2
    temp=out
    if not 1<=temp<=9:
        happy(str(temp),out=0)
    else:
        temp=temp
happy(input('Enter the number:'))
if temp==1:
    print('happy number')
else:
    print('not happy number')    

