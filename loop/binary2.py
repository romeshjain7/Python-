a=int(input('Enter your binary'))
decimal=0
i=0
while a>0:
    if a%10==1:
        decimal+=2**i
        i+=1
    else:
        i+=1
    a//=10
print(decimal)
