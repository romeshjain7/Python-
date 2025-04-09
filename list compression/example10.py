
print([(i,i**2) if  i%4==0  else (i,i**3) for i in range(1,51) if i%2==0])