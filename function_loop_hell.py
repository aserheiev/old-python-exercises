msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

def convert_numbers(number):
    if "." in number:
        try:
            number = float(number)
            return number
        except ValueError:
            print(msg_1)
            get_formula()
    else:
        if not number.isnumeric():
            print(msg_1)
            get_formula()
        else:
            number = int(number)
            return number

def get_formula():
    print(msg_0)
    global num1, oper, num2
    num1, oper, num2 = input().split()
    num1 = convert_numbers(num1)
    num2 = convert_numbers(num2)

get_formula()
print(type(num2))