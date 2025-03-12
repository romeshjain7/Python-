i=1
a=3
def speed():
    global i
    print('hai',i)
    print(a)
    i+=1
    speed()
speed()