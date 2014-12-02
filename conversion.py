#Aaron Bentley
#conversion

def dollars_pounds(amount):
    total = amount * 0.625
    return total

def euro_pounds(amount):
    total = amount * 0.814
    return total

def dollars_euro(amount):
    total = amount * 0.768
    return total

def pound_euro(amount):
    total = amount * 1.229
    return total

def euro_dollars(amount):
    total = amount * 1.302
    return total

def pounds_dollars(amount):
    total = amount * 1.601
    return total

def convert_to_pounds(amount,convert_from):
    if convert_from == "dollar":
        total = dollars_pounds(amount)
    else:
        total = euro_pounds(amount)
    return total

def convert_to_euros(amount,convert_from):
    if convert_from == "dollar":
        total = dollars_euro(amount)
    else:
        total = pound_euro(amount)
    return total

def convert_to_dollars(amount,convert_from):
    if convert_from == "euro":
        total = euro_dollars(amount)
    else:
        total = pounds_dollars(amount)
    return total

def currency_conversion(amount,convert_to,convert_from):
    if convert_to == "pound":
        total = convert_to_pounds(amount,convert_from)
    elif convert_to == "euro":
        total = convert_to_euros(amount,convert_from)
    else:
        total = convert_to_dollars(amount,convert_from)
    return total

def input_():
    amount = int(input("input amount to be converted: "))
    convert_from = input("current currency (euro,pound,dollar): ")
    convert_to = input("currency to be converted to (euro,pound,dollar): ")
    return amount,convert_from,convert_to

def output(total):
    print("total is: {0}".format (total))

def conversion():
    amount,convert_to,convert_from = input_()
    total = currency_conversion(amount,convert_to,convert_from)
    output(total)

#main program

conversion()
