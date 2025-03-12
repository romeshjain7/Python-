str=input('Enter a character')
if 'A'<=str<='Z':
    print(chr(ord(str)+32))
else:
    print(chr(ord(str)-32))