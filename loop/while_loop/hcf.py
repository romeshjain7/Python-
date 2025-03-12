n=int(input('Entera number'))
for i in range(n-1,2,-1):
    if n%i==0:
        print(i)
        break