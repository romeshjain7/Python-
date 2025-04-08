m=int(input('Enter the number of row'))
n=int(input('Enter col no'))

print()
out=[]
for i in range(m):
    inner_list=[]
    for j in range(n):
       inner_list.append(int(input(f'Enter the value for matrix- out[{i}][{j}])')))
    out.append(inner_list)
print(out)