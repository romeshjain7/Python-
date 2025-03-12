inp=int(input('Enter a number'))
if -9<=inp<=9:
    print(f'{inp} is single digit ')
elif -99<=inp<=99 :
    print(f'{inp} is double digit ')
elif -999<=inp<=999:
    print(f'{inp} is triple digit ')
else:
    print(f'{inp} is something else')
