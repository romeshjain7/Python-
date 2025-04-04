print([(i,i**2) if i%2==0 else (i,i**3) for i in range(1,11)])


inp=[10,20,30,40,50]
print([((inp[i]**2)//2)//3 if i%2==0 else ((inp[i]**2)//3)*3 for i in range(0,len(inp))])