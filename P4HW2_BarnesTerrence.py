
# Terrence Barnes Jr.
# 11/1/2026
# P4HW2
# This program calculates regular pay, overtime pay, and gross pay and displays the totals for all workers

"""
Pseudocode:
1. Set the employee count to zero.
2. Set total overtime pay, regular pay, and gross pay to zero.
3. Ask the user to enter an employee's name.
4. While the employee's name is not "Done":
   a. Ask for the employee's pay rate.
   b. Ask for the number of hours worked.
   c. If hours worked are greater than 40:
      - Calculate overtime hours.
      - Calculate regular pay for 40 hours.
      - Calculate overtime pay at 1.5 times the pay rate.
   d. Otherwise:
      - Set overtime hours and overtime pay to zero.
      - Calculate regular pay using hours worked.
   e. Calculate gross pay.
   f. Display the employee's pay information.
   g. Add the employee's pay to the running totals.
   h. Increase the employee count by one.
   i. Ask for the next employee's name.
5. When the user enters "Done":
   a. Display total overtime pay.
   b. Display total regular pay.
   c. Display total gross pay.
   d. Display the total number of employees.
   """

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

employee_name = input("Enter employee's name or Done to terminate: ")

while employee_name != "Done":

    pay_rate = float(input("Enter employee's pay rate: "))
    hours_worked = float(input("Enter number of hours worked: "))

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

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    employee_count += 1

    employee_name = input("\nEnter employee's name or Done to terminate: ")

print("\n----------------------------------------------")
print("Total Overtime Pay: $", format(total_overtime_pay, ".2f"), sep="")
print("Total Regular Pay:  $", format(total_regular_pay, ".2f"), sep="")
print("Total Gross Pay:    $", format(total_gross_pay, ".2f"), sep="")
print("Total Employees:   ", employee_count)
print("----------------------------------------------")
