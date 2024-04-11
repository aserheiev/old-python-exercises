import math
import argparse

def find_i(int_rate):
    global i
    i = (int_rate / 100) / (12)

parser = argparse.ArgumentParser(description = "Sick loan calc")

parser.add_argument("--type", choices = ["annuity", "diff"])
parser.add_argument("--payment", type = float)
parser.add_argument("--principal", type = float)
parser.add_argument("--periods", type = int)
parser.add_argument("--interest", type = float)

args = parser.parse_args()

arg_list = [args.type, args.payment, args.principal, args.periods, args.interest]

if args.interest == None:
    print("Incorrect parameters.")
elif arg_list.count(None) > 1:
    print("Incorrect parameters.")
elif args.type == 'diff':
    if args.payment is not None:
        print("Incorrect parameters.")
    else:
        find_i(args.interest)
        total_pay = 0
        for a in range(1, args.periods + 1):
            diff_pay = math.ceil((args.principal / args.periods) + i * (args.principal - (args.principal * (a - 1) / args.periods)))
            print(f'Month {a}: payment is {diff_pay}')
            total_pay += diff_pay
        print(f'Overpayment = {round(total_pay - args.principal)}')

elif args.type == "annuity":
    if not args.payment:
        find_i(args.interest)
        annuity = math.ceil(args.principal * ((i * pow((1 + i), args.periods)) / (pow((1 + i), args.periods) - 1)))
        overpayment = (annuity * args.periods) - args.principal
        print(f'Your monthly payment = {annuity}!')
        print(f'Overpayment = {int(overpayment)}')
    if not args.principal:
        find_i(args.interest)
        principal = math.floor(args.payment / ((i * math.pow(1 + i, args.periods)) / ((math.pow(1 + i, args.periods) - 1))))
        overpayment = (args.periods * args.payment) - principal
        print(f'Your loan principal = {int(principal)}!')
        print(f'Overpayment = {int(overpayment)}')
    if not args.periods:
        find_i(args.interest)
        months = math.ceil(math.log((args.payment / (args.payment - i * args.principal)), 1 + i))
        years = months // 12
        overpayment = int((months * args.payment) - args.principal)
        if months < 12:
            print(f'It will take {months} to repay this loan!')
            print(f'Overpayment = {overpayment}')
        elif months % 12 == 0:
            print(f'It will take {years} years to repay this loan!')
            print(f'Overpayment = {overpayment}')
        else:
            rem_months = months - years * 12
            print(f'It will take {years} years and {rem_months} months to repay this loan!')
            print(f'Overpayment = {overpayment}')
else:
    print("Incorrect parameters.")