a=int(input('Enter a nhmber:'))
rem=0
i=0
while i<=a:
    rem=str(rem)
    a=a%2
print(f'{ rem[::-1] }')