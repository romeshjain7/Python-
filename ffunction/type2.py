def unique():
    str=input('Enter a string: ')
    rep=()   
    for i in (str):
        c=0
        for j in str:
            if i ==j:
                c+=1
        if c==1:
            rep+=(i,)
    return rep
print(unique())
        
