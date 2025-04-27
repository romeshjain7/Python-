x=int(input("Enter a number"))

def mysum(x):
    total=0
    for i in range(x+1):
        total+=i
    return total
print(mysum(x))


