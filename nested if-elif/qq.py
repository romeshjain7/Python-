# inp='sssssseeeeeewwwww'
# for i in inp:
#     print(i)

# inp=[2,3,1,True,'hello',3]
# out=[9,6,18,18,18,6]

inp=[2,3,1,True,'hello',3]
out=[]
for i in range(len(inp)):
    p=1
    for j in range(len(inp)):
        if i!=j and type(inp[j])==int:
            p*=inp[j]
    out.append(p)
print(out)
    
