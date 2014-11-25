def odd_number():
    number = int(input("enter odd number: "))
    return number
def top(odd_number):
    counter = 1
    if odd_number % 2 == 1:
        while counter <= odd_number:
            list1 = ""
            for count in range(counter):
                list1 = list1 + "*"
            counter = counter + 2
            print("{0:^{1}}".format (list1,odd_number))
def bottom(odd_number):
    counter = odd_number - 2
    while counter > 0:
        list1 = ""
        for count in range(counter):
            list1 = list1 + "*"
        counter = counter - 2
        print("{0:^{1}}".format (list1,odd_number))   
def pyramid():
    number1 = odd_number()
    top(number1),bottom(number1)    
pyramid()
