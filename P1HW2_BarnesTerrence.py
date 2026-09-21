# Terrence Barnes Jr.
# 9/21/2026
# P1HW2.py
# Using VSCode to create and test a program

print("This program calculates and displays travel expenses.")
print("Please enter your budget")
budget = float(input())
print("Please enter your destination of choice")
destination = input()
print("Please enter how much you will spend on gas")
gas_expenses = float(input())
print("Please enter how much you will spend on accommodation")
accommodation_expenses = float(input())
print("Please enter how much you will spend on food")
food_expenses = float(input())

total_expenses = gas_expenses + accommodation_expenses + food_expenses
remaining_budget = budget - total_expenses

print("Travel Expenses:")
print("Destination:", destination)
print("Budget: $", budget)
print("Total Expenses: $", total_expenses)
print("Remaining Budget: $", remaining_budget)