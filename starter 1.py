#Aaron Bentley
#14/11/2014
#starter task 1

def calculate_basic_pay(hours,pay):
    total = hours * pay
    return total

def calculate_overtime_pay(hours,pay):
    overtime_pay = (hours - 40) * (pay*1.5)
    basic_pay = 40 * pay
    total = overtime_pay + basic_pay
    return total

def calculate_total_pay(hours,pay):
    if hours<= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = calculate_overtime_pay(hours,pay)
    return total

def work_details():
    hours = int(input("total hours: "))
    pay = int(input("total pay: "))
    return hours, pay

def display_total_pay(total):
    print(total)
    
def calculate_pay():
    hours,pay = work_details()
    total = calculate_total_pay(hours,pay)
    display_total_pay(total)

calculate_pay()



