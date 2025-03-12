# pn=0
# for i in range(2,100):
#     for j in range(i):
#         if j%i==0:
#             pn=1
#     if pn==1:
#         print(j)
import time
st=time.time()
out=[]
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        out.append(i)
print(out)
en=time.time()
print(en-st)


# a=int(input('Enter a num'))
# i=2
# ind=0
# while i<a:
#     if(a%i==0):
#         ind=1
#     i+=1
# if ind==0:
#     print('prime')
# else:
#     print('not prime')