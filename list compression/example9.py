m=int(input('Enter the number of row'))
n=int(input('Enter col no'))


a=[[int(input(f'Enter the value for a[{i}][{j}]')) for j in range(m)] for i in range(n)]
b=[[int(input(f'Enter the value for b[{i}][{j}]')) for j in range(m)] for i in range(n)]
c=[[(a[i][j]+b[i][j]) for j in range(m)] for i in range(n)]


print()
for i in range(m):
    print('|',end=" ")
    for j in range(n):
       print(a[i][j],end=" ")
    print("|")

print('*'*10)

for i in range(m):
    print('|',end=" ")
    for j in range(n):
       print(b[i][j],end=" ")
    print("|")

print('*'*10)


for i in range(m):
    print('|',end=" ")
    for j in range(n):
       print(c[i][j],end=" ")
    print("|")