# def note(amount):
#     temp=0
#     result=0
#     count_2000
#     remain=0

  
#     return result
# print(note(input('Enter your amount')))
   


   
li=[2000,500,200,100,50,20,10,5,2,1]
dic={}
n=2368 
count=0
for i in li:
    count =n//i
    n=n%i
    dic[i]=count
    count =0
print(dic)