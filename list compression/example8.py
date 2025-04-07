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


print([(i,j) for i in range(3) for j in range(3)])

