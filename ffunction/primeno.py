def prime():
    a=int(input('Enter a num'))
    i=2
    ind=0
    while i<a:
        if(a%i==0):
            ind=1
        i+=1
    if ind==0:
        print('prime')
    else:
        print('not prime')
prime()