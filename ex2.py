#Aaron Bentley
#14/11/2014
#starter task 1

def odd_number():
    number = int(input("enter odd number: "))
    return number

def main(odd_number):
    counter = odd_number
    if odd_number % 2 == 1:
        while counter > 0:
            list1 = ""
            for count in range(counter):
                list1 = list1 + "*"
            counter = counter - 2
            print("{0:^{1}}".format (list1,odd_number))

def display(odd_number):
    main(odd_number)

def pyramid():
    number1 = odd_number()
    main(number1)

pyramid()
    
        
