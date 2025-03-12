def prog(*a):
    fact=1
    for i in a:
        for j in i:
            if type(j)==int:
                fact=1
                for k in range(1,j+1):
                    fact *= k
                print(f'The factorial of {k} is {(fact)}')
            elif type(j)==str:
                print(f'The reverse of {j} is {(j[::-1])}')
            else:
                print(j) 


prog([1,5,7,'hai'],[8,9,'hello',[2,3],[(1,2),3,4,7,'python']])