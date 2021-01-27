print("This is an unit changer\n\n\nThe units which you can change here are: length, weight, and temperature.\n\n")

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
        if change_unit=='kilogram':
            print("Your result is :", int(value) / 10)
        elif change_unit=='quital':
            print("Your result is :", int(value) / 100)
        elif change_unit=='decagram':
            print("Your result is :", int(value) * 10)
        elif change_unit=='gram':
            print("Your result is :", int(value) * 100)
        elif change_unit=='decigram':
            print("Your result is :", int(value) * 1000)
        elif change_unit=='centigram':
            print("Your result is :", int(value) * 10000)
        elif change_unit=='milligram':
            print("Your result is :", int(value) * 100000)
    elif unit=='decigram':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='centigram':
            print("Your result is :", int(value) * 10)
        elif change_unit=='gram':
            print("Your result is :", int(value) / 10)
        elif change_unit=='decagram':
            print("Your result is :", int(value) / 100)
        elif change_unit=='hectogram':
            print("Your result is :", int(value) / 1000)
        elif change_unit=='kilogram':
            print("Your result is :", int(value) / 10000)
    elif unit=='decagram':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='hectogram':
            print("Your result is :", int(value) / 10)
        elif change_unit=='kilogram':
            print("Your result is :", int(value) / 100)
        elif change_unit=='gram':
            print("Your result is :", int(value) * 10)
        elif change_unit=='decigram':
            print("Your result is :", int(value) * 100)
        elif change_unit=='centigram':
            print("Your result is :", int(value) * 1000)
        elif change_unit=='quintal':
            print("Your result is :", int(value) / 1000)
    elif unit=='gram':
        change_unit = input("Enter an another unit for changing(Enter full name like -metre)")
        if change_unit=='centigram':
            print("Your result is :", int(value) * 100)
        elif change_unit=='kilogram':
            print("Your result is :", int(value) / 1000)
        elif change_unit=='decagram':
            print("Your result is :", int(value) / 10)
        elif change_unit=='hectogram':
            print("You result is :", int(Value) / 100)
        elif change_unit=='decigram':
            print("Your result is :", int(value) * 10)
        elif change_unit=='microgram':
            print("Your result is :", int(value) * 1000000)
        elif change_unit=='quintal':
            print("Your result is :", int(value) / 10000)
    elif unit=='centimetre':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='milligram':
            print("Your result is :", int(value) * 10)
        elif change_unit=='decigram':
            print("Your result is :", int(value) / 10)
        elif change_unit=='gram':
            print("Your result is :", int(value) / 100)
        elif change_unit=='decagram':
            print("Your result is :", int(value) / 1000)
        elif change_unit=='hectogram':
            print("Your result is :", int(value) / 10000)
        elif change_unit=='kilogram':
            print("Your result is :", int(value) / 100000)
        elif change_unit=='microgram':
            print("Your result is :", int(value) * 10000)
elif quantity=='temperature':
    value = int(input("Enter a value or a number"))
    unit = input("Enter an unit of the entered number(Enter the full name like -metre) :")
    if unit=='celsius':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='kelvin':
            print("Your result is :", int(value) + 273.15)
        elif change_unit=='fahrenheit':
            f = int(value) * 9/5
            print("Your result is :", int(f) + 32)
    elif unit=='kelvin':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='celsius':
            print("Your reault is :", int(value) - 273.15)
        elif change_unit=='fahrenheit':
            h = int(value) - 273.15
            j = int(h) * 9/5
            k = int(j) + 32
            print("Your result is :", int(k))
    elif unit=='fahrenheit':
        change_unit = input("Enter a another unit for changing(Enter full name like -metre) :")
        if change_unit=='celsius':
            i = int(value) - 32
            p = int(i) * 5/9
            print("Your result is :", int(p))
        elif change_unit=='kelvin':
            o = int(value) - 32
            a = int(o) * 5/9
            y = int(a) + 273.15
            print("Your result is :", int(y))

        
        
