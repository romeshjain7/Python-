def outer():
    a=10
    b=20
    print(a+b)
    def inner():
        p='hai'
        q='hello'
        print(p+q)
        def inner2():
            r=[1,2,3,4,5]
            print(r[::-1])
        inner2() 
    inner()
outer()