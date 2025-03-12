theory_mark=int(input('Enter you theory mark'))
practical_mark=int(input('Enter you pratical mark'))
total_mark=theory_mark+practical_mark
if total_mark>=50:
    if 35<=theory_mark<=70:
        if 15<=practical_mark<=30:
            
            print('Passed')
else:
    print('Failed, try again')