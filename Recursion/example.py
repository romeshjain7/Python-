# inp=[[1,2,'a',3],[3,'5','7',4],[6,8,(1,),3]]
# out=[]
# sum=0
# for i in inp:
#     for j in i:
#         if type(j)==int:
#             sum=sum+j
# print(sum)

def sumofList(inp):
    out=0
    for i in inp:
        if type(i)==int:
            out+=i
        elif type(i)==list:
            out+=sumofList(i)
    return out 
print(sumofList([[1,2,'a',3,[3,4],[4,6,7]],[3,'5','7',4],[6,8,(1,),3]]))