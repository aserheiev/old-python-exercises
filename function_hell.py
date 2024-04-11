msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

def convert_numbers(number):
    if "." in number:
        try:
            number = float(number)
            return number
        except ValueError:
            return None
    else:
        if not number.isnumeric():
            return None
        else:
            number = int(number)
            return number

def get_formula():
    print(msg_0)
    global num1, oper, num2
    num1, oper, num2 = input().split()
    num1 = convert_numbers(num1)
    num2 = convert_numbers(num2)
    if num1 == None or num2 == None:
        print(msg_1)
        get_formula()

def check_operand(operand):
    if (operand != "+") and (operand != "-") and (operand != "*") and (operand != "/"):
        print(msg_2)
        get_formula()

def calculate(number_1, operand, number_2):
    if operand == "+":
        print(float(number_1 + number_2))
    if operand == "-":
        print(float(number_1 - number_2))
    if operand == "*":
        print(float(number_1 * number_2))
    if operand == "/":
        if number_2 == 0:
            print(msg_3)
            get_formula()
            calculate(num1, oper, num2)
        else:
            print(float(number_1 / number_2))


get_formula()
check_operand(oper)
calculate(num1, oper, num2)