n=['pythhon','is','good']
res=[]
for i in range(0,len(n)):
    for j in n[i]:
        if n[i] not in 'aeiouAEIOU':
            res=res.append(n[i])
print(res)