# def fact(n):
#     out=[]
#     length=len(n)
#     fact=1
#     sol=[]

#     for k in range(length):
#         if n ==1:
#             fact= 1
#         fact= n* fact(n-1)

#     for i in 
   
# def permut(a,i=0):
#     if i==len(a):
#         print(a)
#     for j in range(i,len(a)):
#         w=list(a)
#         w[i],w[j]=w[j],w[i]
#         permut(w,i+1)
# permut('abcd')

from itertools import permutations,combinations
print(list(permutations('abcd')))
print(len(list(permutations('abcd'))))
print(list(combinations([1,2,3],2)))
