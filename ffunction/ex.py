str=input('Enter a string: ')
rep=[]     
 for i in (str):
        if i not in rep:
            rep=rep.append(i)
        else:
            break