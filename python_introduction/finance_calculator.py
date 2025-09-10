#!/usr/bin/python3

income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

savings =  income - expenses
annual_savings = savings * 12 + (savings * 12 * 0.05)

print("Your monthly savings are ${}.".format(savings))
print("Projected savings after one year, with interest, is: ${}.".format(annual_savings))
