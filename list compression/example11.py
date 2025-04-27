# out={}
# for i in range(1,27):
#     out[i]=chr(i+64)
# print(out)
#  #! dict comphrehension
# {key:value for var in iterable if <condition>}
# print({ i:chr(i+64) for i in range(1,27)})
# print({ chr(i+64):chr(91-i) for i in range(1,27)})
# print({ chr(i+64):chr(i+64+32) for i in range(1,27)})
# print({ i:i*(chr(i+64))+i*(chr(i+64+32)) for i in range(1,27)})


# print({i:i**2 if i%2==0 else i**3  for i in range(1,11)})
# {chr(ord(65)):chr(ord(i+32) for i in range(65,91))}


print({i: i.upper() if 'a'<=i<='z' else i.lower()  for i in 'pYtHoN'})
