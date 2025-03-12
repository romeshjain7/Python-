import random
n=random.randint(1,100)
print(n)   #just for understanding 
for i in range(5,0,-1):
    guess=int(input('Enter your number'))
    if guess==n:
        print('you got the number')
        break;
    else:
        print('you can not get the number')
    if i==1:
        print('you lost the game')