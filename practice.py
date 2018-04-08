LoanAmount = float(input("Enter Loan Amount: "))
InterestRate = 0.05
NumberOfpayment = int(input("Enter Number of Payment: "))
MonthlyPayment = LoanAmount*InterestRate*(1+InterestRate)**NumberOfpayment/\
                ((1+InterestRate)**NumberOfpayment-1)
print(MonthlyPayment)

import datetime 
CurrentDate = datetime.date.today()
ProjectDeadline = input("enter project deadline dd/mm/yyy: ")
DaysToFinish = datetime.datetime.strptime(ProjectDeadline, '%d/%b/%Y').date()
print(DaysToFinish)