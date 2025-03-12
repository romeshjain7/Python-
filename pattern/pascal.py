# n=int(input('Enter a number'))
# list2=[]
# for i in range (n):
#     list=[]
#     if i>0:
#         for j in range(1,i):
#             list.append(print(list2[j-i]+list2[j]))
#         list.append(1)
#     print(list)

# n=[5,4,2,4,5,5,6,7]
# newVal=0
# for i in range(len(n)-1):
#     newVal=n[i]+n[i+1]

#     # print(n[i], end=' ')
#     print(newVal, end=' ')

inp=int(input('Enter a number'))
k=[]
for i in range(inp):
    l=[]
    for j in range(i+1):
        if j==0 or j==i:
            l.append(1)
        else:
            l.append(k[i-1][j-1]+k[i-1][j])
    k.append(l)
print(k)

m=str(k)
print(m)