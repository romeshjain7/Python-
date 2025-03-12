day=int(input('Enter your date (DD):'))
month=input('Enter your month (month):')
year=int(input('Enter your year (YYYY):'))
date=(day,month,year)
print(date)
if (year%4==0 and year%100!=0) or year%400==0:
    print('Feb has 29 days and it is a leap year')
else:
    print('it is not a leap year and feb has 28 days')
if month=='Feb':
    if (year%4==0 and year%100!=0) or year%400==0:
        print('Feb has 29 days')
    else:
        print('Feb has 28 days')

elif month in ('April','June','September','November'):
    print(f'{month} has 30 days')
else:
    print(f'{month} has 31 days')




