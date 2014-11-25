#Aaron Bentley
#25/11/14
#revision ex 1
def input_integer():
    integer = int(input("Input number of times to be repeated: "))
    return integer

def input_character():
    character = input("Input character: ")
    return character

def lists(integer,character):
    list_1 = ""
    for count in range(integer):
        list_1 = list_1 + character
    return list_1

def display(list_1):
    print(list_1)

def output_symbols():
    integer = input_integer()
    character = input_character()
    list_1 = lists(integer,character)
    display(list_1)

output_symbols()
