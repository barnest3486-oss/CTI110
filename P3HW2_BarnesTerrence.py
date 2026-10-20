# Terrence Barnes Jr.
# 10/19/2026
# P3HW2
# This program calculates an employee's regular pay, overtime pay, and gross pay.

"""
Pseudocode:
1. Ask the user to enter the employee's name.
2. Ask the user to enter the number of hours worked.
3. Ask the user to enter the employee's hourly pay rate.
4. If hours worked are greater than 40:
   a. Calculate overtime hours by subtracting 40 from hours worked.
   b. Calculate regular pay for 40 hours.
   c. Calculate overtime pay at 1.5 times the regular hourly rate.
5. Otherwise:
   a. Set overtime hours and overtime pay to zero.
   b. Calculate regular pay using the hours worked.
6. Calculate gross pay by adding regular pay and overtime pay.
7. Display the employee name, hours worked, pay rate, overtime hours,
   overtime pay, regular pay, and gross pay.
"""

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_pay = 40 * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
else:
    overtime_hours = 0
    regular_pay = hours_worked * pay_rate
    overtime_pay = 0

gross_pay = regular_pay + overtime_pay

print("----------------------------------------------")
print(f"Employee name:    {employee_name}")
print()
print(f"{'Hours Worked':<18}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<18}{'RegHour Pay':<18}{'Gross Pay':<12}")
print("-" * 96)
print(f"{hours_worked:<18.1f}${pay_rate:<14.2f}{overtime_hours:<15.1f}${overtime_pay:<17.2f}${regular_pay:<17.2f}${gross_pay:.2f}")
