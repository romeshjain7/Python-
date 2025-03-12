input=input('Enter a character')
if 'a'<=input<='z':
    print(f'{input} is a lower case character')
elif 'A'<=input<='Z':
    print(f'{input} is a upper case character')
elif '0'<=input<='9':
    print(f'{input} is a number character')
else:
    print(f'{input} is a special character')