a=int(input('Enter a number'))
i=1
big=i
while i<=a:
        if a%i==0:
            print(i)
            big=i
        i=i+1
print(f'Biggest common factor is {big}')
        