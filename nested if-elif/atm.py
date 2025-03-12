a=input('Enter you password')
correct_pwd='1111'
if len(a)==4:   
    if correct_pwd==a:
        print('correct password,logged in succesfully')
    else:
        print('Wrong password,please try again')
        a=input('Enter you password')
        if correct_pwd==a:
            print("Successfully logged in 2nd chance")
        else:
             print('Wrong password,please try again')
        a=input('Enter you password')
        if correct_pwd==a:
            print("Successfully logged in 3nd chance")
        else:
            print('failed in 3rd chance')
else:
    print('invalid password')