for i in range(1,6):
    for j in range(1,6):
        print(j, end=" ")
    print()

print()

for i in range(1,6):
    for j in range(1,6):
        print(i, end=" ")
    print()

print()

n=1
for i in range(1,6):
    for j in range(1,6):
        print(n,end=" ")
        n+=1
    print()

print()

for i in range(5):
    for j in range(5):
        if i==j:
            print('1' ,end=" ")
        else:
            print('0', end=" ")
    print()

print()

m= int(input('ENter anumber'))
for i in range(1,m):
    for j in range(1,m):
        if i+j==m:
            print('1' ,end=" ")
        else:
            print('0', end=" ")
    print()

m= int(input('ENter anumber'))
for i in range(1,m):
    for j in range(1,m):
        if i+j==m or i==j:
            print('1' ,end=" ")
        else:
            print('0', end=" ")
    print()


print()

m= int(input('ENter anumber'))
for i in range(1,m):
    for j in range(1,m):
        if i+j==m or i==j:
            print('1' ,end=" ")
        else:
            print( " ", end=" ")
    print()


