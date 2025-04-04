# [chr(i) for  i in range(ord('A'),ord('z')+1)and range(ord('a'),ord('z')+1)]
# s='oython'
# [s[i+2]for i in s]
inp='python'
print([inp[i] for i in range(len(inp)) if i%2==0])
