

# m= int(input('ENter anumber'))
# for i in range(1,m):
#     for j in range(1,m):
#         if i+j>=m or i==j:
#             print('*' ,end=" ")
#         else:
#             print( " ", end=" ")
#     print()``

# m= int(input('ENter anumber'))
# for i in range(1,m):
#     for j in range(1,m):
#         if i+j<=m or i==j:
#             print('*' ,end=" ")
#         else:
#             print( " ", end=" ")
#     print()


# m= int(input('ENter anumber'))
# for i in range(1,m):
#     for j in range(1,m):
#         if i>j or i+j==6 or i==j:
#             print('*' ,end=" ")
#         else:
#             print( " ", end=" ")
#     print()


# m= int(input('ENter anumber'))
# for i in range(1,m):
#     for j in range(1,m):
#         if i<j or i+j==m or i==j: 
#             print('*' ,end=" ")
#         else:
#             print( " ", end=" ")
#     print()

m= int(input('ENter anumber'))
for i in range(1,m):
    for j in range(1,m):
        if i<j or i+j==m or i==j: 
            print('*' ,end=" ")
        else:
            print( " ", end=" ")
    print()
