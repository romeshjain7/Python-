str=eval(input('Enter character or number'))
print(type(str))
if 65<=ord(str)<=90 and len(str)==1:
    print(f'{str} is upper case')
elif 'a'<=str<='z' and len(str)==1:
    print(f'{str} is lower case')
elif type(str)==int:
    print('dfd')  #print ascii value
