# def uppercase(n):
#     out=''
#     # n=list(n)
#     for  i in n:
#         if i ==i.upper():
#             out+=i
#     return out
# print (uppercase('heLlLLYFDbmddkHSOC'))



# def upper(inp , i=0 ,out=''):
#     if i>=len(inp):
#         return out 
#     if 'A' <=inp[i]<='Z':
#         out+=inp[i]
#     return upper(inp,i+1,out)
# print(upper('A'))
# print(upper('AklfIJIDJIKnncosUnccnIH'))

def upper(inp , i=0 ,out=''):
    if i>=len(inp):
        return out 
    if 'A' <=inp[i]<='Z':
        out+=inp[i].lower()
    else:
        out+=inp[i].upper()
    return upper(inp,i+1,out)
print(upper('A'))
print(upper('AklfIJIDJIKnncosUnccnIH'))