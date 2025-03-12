a=eval(input('Enter a value'))
dict1={1:'one-hundred',2:'two-hundred',3:'three-hundred',4:'four-hundred'}
dict2={0='',1:'tt',2:'twenty',3:'thirty',4:'forty'}
dict3={0:'',1:'one',2:'two',3:'three',4:'four'}
if type(a)==int:
    if 100<=a<=999:
        b=a%10
        c=(a//10)%10
        d=a//100
        print(f'{b}{c}{d}') #reverse three digit no.
        print(f'{dict1.get(d)}{dict2.get(c)}{dict3.get(b)}')
    else:
else:
    print(f'{a} is not a three digit integer')



