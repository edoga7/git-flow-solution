


#def age_calculator():
    #name = input("What is your name: ")
    #age = int(input("How old are you: "))
    #year = str((2018 - age)+100)
    #print(name + " will be 100 years old in the year " + year)

#age_calculator()

#obiora = input("in 2018 he will be: ")
#if obiora.isdigit():
   # print(obiora , "the age is \n correct")
#else:
    #print(obiora , "not correct")





#num = int(input("what is the number: "))
#x = num % 2
#if x > 0:
   # print("even number")
#else: 
   # print("odd number")

#loan calculator
#formular ; M = L[i(1+i)n] / [(1+i)n-1] 
# M = Monthly payment
# L = loan amount
# i = intrest rate (0.05)
# n = number of payment 
# LoanAmount = input("Enter Loan Amount: ")
# InterestRate = 0.05
# NumberOfpayment = input("Enter Number of Payment: ")
# MonthlyPayment = float(LoanAmount) *float(InterestRate) * (1 + float(InterestRate)) * int(NumberOfpayment) / (1 + float(InterestRate)) * int(NumberOfpayment) -1 
# print(MonthlyPayment)

# LoanAmount = float(input("Enter Loan Amount: "))
# InterestRate = 0.05
# NumberOfpayment = int(input("Enter Number of Payment: "))
# MonthlyPayment = LoanAmount*InterestRate*(1+InterestRate)**NumberOfpayment/\
#                 ((1+InterestRate)**NumberOfpayment-1)
# print(MonthlyPayment)

# LoanAmount = input("Enter Loan Amount: ")
# InterestRate = 0.05
# NumberOfpayment = input("Enter Number of Payment: ")
# MonthlyPayment = float(LoanAmount)*float(InterestRate)*(1+float(InterestRate))**(1+int(InterestRate))**int(NumberOfpayment)-1
# print(MonthlyPayment)

# name = input("what is your name?: ")
# name = name.upper()
# country = input("which country are you from: ")
# occupation = input("and what occupation?: ")
# print("Mr" , name , "is from", country , "and he works as an" , occupation , "consultant at XYZ")

from datetime import datetime 
CurrentDate = datetime.now()
print(CurrentDate)
ProjectDeadline = input("enter project deadline mm/dd/yyy: ")
DaysToFinish = datetime.strptime(ProjectDeadline, '%d/%m/%Y %I:%M%p')
print(DaysToFinish)
outstandingDay = DaysToFinish - CurrentDate  
print(outstandingDay)

