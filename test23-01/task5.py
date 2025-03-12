salary=int(input('Please enter your salary:'))
cc_score=int(input('Please enter you credit score:'))
loan_ammount=int(input('Please enter your loan ammount:'))

if salary>+50000:
    if cc_score>750:
        if loan_ammount>20*salary:
            print('Loan Approved')
else:
    print('Loan is not approved')