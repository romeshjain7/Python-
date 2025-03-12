a=[1,2,3,4,5,6,7]
i=0
total=[]
mid=(len(a)//2)+1
new_length=mid
while new_length<=len(a):
    print(a[new_length])
    new_length+=1
while i<new_length:
    print(a[i])
    new_length+=1
total=new_length+mid
print(total)

# out=[5,6,7,4,1,2,3]


inp='Roses are Red'
out={'Roses':5,'are':3,'Red':3}
out{'sesoR':2,'era':2,'deR':1}