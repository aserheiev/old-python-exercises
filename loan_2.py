import math

print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
choice = input(">")

def find_i(int_rate):
    global i
    i = (int_rate / 100) / (12)
    
if choice == "n":
    loan_principal = float(input("Enter the loan principal:\n> "))
    monthly_pay = float(input("Enter the monthly payment:\n> "))
    interest = float(input("Enter the loan interest:\n> "))
    find_i(interest)
    months = math.ceil(math.log((monthly_pay / (monthly_pay - i * loan_principal)), 1 + i))
    if months < 12:
        print(f'It will take {months} to repay this loan!')
    else:
        years = months // 12
        rem_months = months - years * 12
        print(f'It will take {years} years and {rem_months} months to repay this loan!')
    
if choice == "a":
    loan_principal = float(input("Enter the loan principal:\n>"))
    periods = int(input("Enter the number of periods:\n>"))
    interest = float(input("Enter the loan interest:\n>"))
    find_i(interest)
    annuity = math.ceil(loan_principal * ((i * pow((1 + i), periods)) / (pow((1 + i), periods) - 1)))
    print(f'Your monthly payment = {annuity}!')

if choice == "p":
    annuity = float(input("Enter the annuity payment:\n>"))
    periods = int(input("Enter the number of periods:\n>"))
    interest = float(input("Enter the loan interest:\n>"))
    find_i(interest)
    principal = round(annuity / ((i * math.pow(1 + i, periods)) / ((math.pow(1 + i, periods) - 1))))
    print(f'Your loan principal = {principal}!')