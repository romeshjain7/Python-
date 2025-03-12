n=5
out=[]
s=0
d=0
for i in range(1,n+1):
    out.append('1'*i)
    s+=int(out[-1])
    
print(out)
print(s)