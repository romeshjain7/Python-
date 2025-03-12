# n=int(input('Enter a number'))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")

    
#     print()

# n=int(input('Enter a number'))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print(j,end=" ")
#         else:
#             print(' ',end=" ")

    
#     print()


# n=int(input('Enter a number'))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print(i,end=" ")
#         else:
#             print(' ',end=" ")

    
#     print()


# n=int(input('Enter a number'))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print(i+j,end=" ")
#         else:
#             print(' ',end=" ")

    
#     print()


# n=int(input('Enter a number'))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print(i*j,end=" ")
#         else:
#             print(' ',end=" ")

    
#     print()

n=int(input('Enter a number'))
m=(n//2)
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==m or j==m:
            print("*",end=" ")
        else:
            print(' ',end=" ")

    
    print()