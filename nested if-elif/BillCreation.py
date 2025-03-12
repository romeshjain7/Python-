print('Please order your fav. pizza')

pizza_option={1:['Veg Pizza',99], 2:['Cheese Pizza',129], 3:['Chicken Pizza',159] ,4:['Pasta Pizaa',199]}
choice=int(input(f'Enter 1 to choice {pizza_option.get(1)[0]} \n Enter 2 to choice {pizza_option.get(2)[0]} \n Enter 3 to choice {pizza_option.get(3)[0]} \n Enter 4 to choice {pizza_option.get(4)[0]}'))
quantity=int(input('Enter you quantity'))
total=0


if choice ==1:
    print(f'You choice is{pizza_option.get(1)[0]} and account is {(pizza_option.get(1)[1]*quantity)}') 
elif choice ==2:
    print(f'You choice is{pizza_option.get(1)[0]} and account is {(pizza_option.get(1)[1]*quantity)}') 
elif choice ==3:
    print(f'You choice is{pizza_option.get(1)[0]} and account is {(pizza_option.get(1)[1]*quantity)}') 
elif choice ==4:
    print(f'You choice is{pizza_option.get(1)[0]} and account is {(pizza_option.get(1)[1]*quantity)}')

total=(pizza_option.get(1)[1]*quantity)
print(f'Total account as of now is ₹{total}')
      
print('Do you want to add more pizza')
add_more_pizza=int(input("Enter 1 to 'Yes' \n Enter 2 to 'NO'"))
choice=int(input(f'Enter 1 to choice {pizza_option.get(1)[0]} \n Enter 2 to choice {pizza_option.get(2)[0]} \n Enter 3 to choice {pizza_option.get(3)[0]} \n Enter 4 to choice {pizza_option.get(4)[0]}'))
if add_more_pizza==1:
    if choice ==1:
        print(f'You choice is{pizza_option.get(1)[0]} and account is {(pizza_option.get(1)[1]*quantity)}') 
    elif choice ==2:
        print(f'You choice is{pizza_option.get(1)[0]} and account is {(pizza_option.get(1)[1]*quantity)}') 
    elif choice ==3:
        print(f'You choice is{pizza_option.get(1)[0]} and account is {(pizza_option.get(1)[1]*quantity)}') 
    elif choice ==4:
        print(f'You choice is{pizza_option.get(1)[0]} and account is {(pizza_option.get(1)[1]*quantity)}')

total= total+(pizza_option.get(1)[1]*quantity)
print(f'Total account as of now is ₹{total}')

if add_more_pizza==0:
    total= total+(pizza_option.get(1)[1]*quantity)
    print(f'Total account as of now is ₹{total}')

print('Do you want add-on')
add_on=int(input("Enter 1 to 'Yes' \n Enter 2 to 'NO'"))
add_on_option={1:['Dip',19], 2:['Cheese Burst',59], 3:['Special',79] ,4:['Extra-Corn',99]}
add_on_choice=int(input(f'Enter 1 to choice {add_on_option.get(1)[0]} \n Enter 2 to choice {add_on_option.get(2)[0]} \n Enter 3 to choice {add_on_option.get(3)[0]} \n Enter 4 to choice {add_on_option.get(4)[0]}'))

if add_on_choice ==1:
    print(f'You choice is {add_on_option.get(1)[0]} and account is ₹{(add_on_option.get(1)[1])}') 
if add_on_choice ==2:
    print(f'You choice is {add_on_option.get(1)[0]} and account is ₹{(add_on_option.get(1)[1])}') 
if add_on_choice==3:
    print(f'You choice is {add_on_option.get(1)[0]} and account is ₹{(add_on_option.get(1)[1])}') 
if add_on_choice ==4:
    print(f'You choice is {add_on_option.get(1)[0]} and account is ₹{(add_on_option.get(1)[1])}')

total=total+(add_on_option.get(1)[1])
print(f'Thank you for ordering \n You total bill is ₹{total}')