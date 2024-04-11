msg_list = \
        ["Enter an equation", \
        "Do you even know what numbers are? Stay focused!", \
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?", \
        "Yeah... division by zero. Smart move...", \
        "Do you want to store the result? (y / n):", \
        "Do you want to continue calculations? (y / n):", \
        " ... lazy", " ... very lazy", " ... very, very lazy", "You are", \
        "Are you sure? It is only one digit! (y / n)", \
        "Don't be silly! It's just one number! Add to the memory? (y / n)", \
        "Last chance! Do you really want to embarrass yourself? (y / n)"]
mem = 0

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

def is_one_digit(v):
    if type(v) == float:
        if v > -10 and v < 10 and v.is_integer():
            output = True
        else:
            output = False
        return output
    elif type(v) == int:
        if v > -10 and v < 10:
            output = True
        else:
            output = False
        return output

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_list[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_list[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_list[8]
    if msg != "":
        msg = msg_list[9] + msg
        print(msg)  

def check_operand(operand):
    if (operand != "+") and (operand != "-") and (operand != "*") and (operand != "/"):
        print(msg_list[2])
        get_formula()

def calculate(number_1, operand, number_2):
    global result
    if operand == "+":
        result = float(number_1 + number_2)
    if operand == "-":
        result = float(number_1 - number_2)
    if operand == "*":
        result = float(number_1 * number_2)
    if operand == "/":
        if number_2 == 0:
            print(msg_list[3])
            get_formula()
            calculate(num1, oper, num2)
        else:
            result = float(number_1 / number_2)
    return result

def get_formula():
    print(msg_list[0])
    global num1, oper, num2, mem
    num1, oper, num2 = input().split()
    if num1 == "M":
        num1 = mem
    else:
        num1 = convert_numbers(num1)
    if num2 == "M":
        num2 = mem
    else:
        num2 = convert_numbers(num2)
    if num1 == None or num2 == None:
        print(msg_list[1])
        get_formula()
    check_operand(oper)

def memoryloop():
    global mem, result
    if input(msg_list[4]) == "y":
        if not is_one_digit(result):
            mem = result
        else:
            msg_index = 10
            while msg_index < 13:
                if input(msg_list[msg_index]) == "y":
                    msg_index += 1
                else:
                    break
            if msg_index == 13:
                mem = result
    if input(msg_list[5]) == "y":
        jankcalc()

def jankcalc():
    global result
    get_formula()
    check(num1, num2, oper)
    result = calculate(num1, oper, num2)
    print(result)
    memoryloop()


jankcalc()