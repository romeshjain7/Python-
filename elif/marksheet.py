percentage=float(input('Enter your percentage:'))
if percentage>=85:
    print('Distinction')
elif 70<percentage<85:
    print('First class')
elif 60<percentage<70:
    print('second class')
elif 40<=percentage<=60:
    print('just pass')
else:
    print('fail')