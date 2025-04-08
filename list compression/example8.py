#write the program to check the no is even and multiple of 4 if it is square , if not cube 



# print([(i,i**2) if  i%4==0  else (i,i**3) for i in range(1,51) if i%2==0])


# print([(i,i*w) for i in range(1,1001) for w in range(1,8) if i%2!=0])

# print([i if i%7==0 else (i,i*7,i)  if i%5==0 else (i,i*5,i)   if i%3==0   else (i,i*3,i) for i in range(1,106) ] )


# print([(i) for i in range(3) for w in range(3)])
# print([(w) for i in range(3) for w in range(3)])


# out=[]
# for i in range(3):
#     out_q=[]

#     for j in range(3):
#         out_q.append(i)
#     out.append(out_q)
# print(out)


# print([[(i) for w in range(3)] for i in range(3)])
# print([[(i,w) for w in range(3)] for i in range(3)])


# print([(i,j) for i in range(3) for j in range(3) ])
# print([(i,j) for i in range(5) for j in range(5) if i!=j])
# print([(i,j)for i in range(5 )  for j in range(5)  if i<j ])
# print([[(i,j)for j in range(5 ) if i<j ] for i in range(5)   ])
# print([[(i,i*j)for j in range(1,11 ) ] for i in range(2,11)   ])


# print([1 if i==j else 0  for i in range(3)  for j in range(3)])
# print([[1 if i==j else 0  for j in range(3) ] for i in range(3)])
# print([['S' if i==j else 'O'  for j in range(3) ] for i in range(3)])



# print([(i,j)  for i in range(5) for j in range(5) if(i+j)%2==0 ])
# print([[(i,j)  for j in range(5) if(i+j)%2==0]for i in range(5)  ])


m=int(input('Enter the number of row'))
n=int(input('ENter col no'))
# list=[[1 if i==j else 0  for j in range(m) ] for i in range(n)]
# print([[1 if i==j else 0  for j in range(m) ] for i in range(n)])

print()
out=[]
for i in range(m):
    inner_list=[]
    for j in range(n):
       inner_list.append(int(input(f'Enter the value for matrix- out[{i}][{j}])')))
    out.append(inner_list)
print(out)

# n,m=m,n
# out2=[]
# for i in range(m):
#     inner2=[]
#     for j in range(n):
#         inner2.append(out[i][j])
#     out2.append(inner2)
# print(out2)
# print(out[::-1])

# a=[[int(input(f'Enter the value for a[{i}][{j}]')) for j in range(m)] for i in range(n)]
# for i in range(m):
#     print('|',end=" ")
#     for j in range(n):
#        print(a[i][j],end=" ")
#     print("|")
# # print(a)

# A=[[(int(input(f'Enter the value for [{i}][{j}]:') )) for j in range(n)] for i in range(m) ]
# print(A)


# A=[((int(input(f'Enter the value for [{i}][{j}]:') ))  for j in range(n)) for i in range(m) for k in range(n) ]
# print(A)

