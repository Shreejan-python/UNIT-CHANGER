print("This is an unit changer\n\n\nThe units which you can change here are: length, weight, litres, temperature and time.\n\n")

quantity = input("Enter a quantity which you want to change(For ex- length, litres, etc) :")
if quantity=='length':
    value = int(input("Enter a value or a number"))
    unit = input("Enter an unit of the entered number(Enter the full name like -metre) :")
    if unit=='centimetre':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='millimetre':
            print("Your result is :", int(value) * 10)
        elif change_unit=='decimetre':
            print("Your result is :", int(value) / 10)
        elif change_unit=='metre':
            print("Your result is :", int(value) / 100)
        elif change_unit=='decametre':
            print("Your result is :", int(value) / 1000)
        elif change_unit=='hectometre':
            print("Your result is :", int(value) / 10000)
        elif change_unit=='kilometre':
            print("Your result is :", int(value) / 100000)
        elif change_unit=='micrometre':
            print("Your result is :", int(value) * 10000)
    elif unit=='metre':
        change_unit = input("Enter an another unit for changing(Enter full name like -metre)")
        if change_unit=='centimetre':
            print("Your result is :", int(value) * 100)
        elif change_unit=='kilometre':
            print("Your result is :", int(value) / 1000)
        elif change_unit=='decametre':
            print("Your result is :", int(value) / 10)
        elif change_unit=='hectometre':
            print("You result is :", int(Value) / 100)
        elif change_unit=='decimetre':
            print("Your result is :", int(value) * 10)
        elif change_unit=='micrometre':
            print("Your result is :", int(value) * 1000000)    
        
    elif unit=='kilometre':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='hectometre':
            print("Your result is :", int(value) / 10)
        elif change_unit=='decametre':
            print("Your result is :", int(value) / 100)
        elif change_unit=='metre':
            print("Your result is :", int(value) / 1000)
        elif change_unit=='decimetre':
            print("Your result is :", int(value) / 10000)
        elif change_unit=='centimetre':
            print("Your resulr is :", int(value) / 100000)

    elif unit=='hectometre':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='kilometre':
            print("Your result is :", int(value) / 10)
        elif change_unit=='decametre':
            print("Your result is :", int(value) * 10)
        elif change_unit=='metre':
            print("your result is :", int(value) * 100)
        elif change_unit=='decimetre':
            print("Your result is :", int(value) * 1000)
        elif change_unit=='metre':
            print("Your result is :", int(value) * 10000)
        elif change_unit=='centimetre':
            print("Your result is :", int(value) * 100000)
    elif unit=='decametre':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='hectometre':
            print("Your result is :", int(value) / 10)
        elif change_unit=='kilometre':
            print("Your result is :", int(value) / 100)
        elif change_unit=='metre':
            print("Your result is :", int(value) * 10)
        elif change_unit=='decimetre':
            print("Your result is :", int(value) * 100)
        elif change_unit=='centimetre':
            print("Your result is :", int(value) * 1000)
    elif unit=='decimetre':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='centimetre':
            print("Your result is :", int(value) * 10)
        elif change_unit=='metre':
            print("Your result is :", int(value) / 10)
        elif change_unit=='decametre':
            print("Your result is :", int(value) / 100)
        elif change_unit=='hectometre':
            print("Your result is :", int(value) / 1000)
        elif change_unit=='kilometre':
            print("Your result is :", int(value) / 10000)
elif quantity=='weight':
    value = int(input("Enter a value or a number"))
    unit = input("Enter an unit of the entered number(Enter the full name like -metre) :")
    if unit=='kilogram':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='quintal':
            print("Your result is :", int(value) / 100)
        elif change_unit=='hectogram':
            print("Your result is :", int(value) * 10)
        elif change_unit=='decagram':
            print("Your result is :", int(value) * 100)
        elif change_unit=='gram':
            pritn("Your result is :", int(value) * 1000)
        elif change_unit=='decigram':
            print("Your result is :", int(value) * 10000)
        elif change_unit=='centigram':
            print("Your result is :", int(value) * 100000)
    elif unit=='quintal':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='kilogram':
            print("Your result is :", int(value) * 100)
        elif change_unit=='hectogram':
            print("Your result is :", int(value) * 1000)
        elif change_unit=='decagram':
            print("Your result is :", int(value) * 10000)
        elif change_unit=='gram':
            print("Your result is :", int(value) * 100000)
        elif change_unit=='decagram':
            print("Your result is :", int(value) * 1000000)
        elif change_unit=='centigram':
            print("Your result is :", int(value) * 10000000)
    elif unit=='hectogram':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")

        
