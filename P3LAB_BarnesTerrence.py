# Terrence Barnes Jr.
# P3LAB
# 10/18/2026
# Money Counter

#
# Pseudocode:
# Ask the user to enter an amount of money.
# Convert the amount to cents.
# Calculate the number of dollars.
# Subtract the dollar value from the remaining cents.
# Calculate the number of quarters, dimes, nickels, and pennies.
# Display only the coins and bills that are needed.
# Display the singular name if the amount is one.
# Display the plural name if the amount is more than one.
# If the amount is zero, display No change.

amount = float(input("Enter the amount of money as a float: $"))

# Convert dollars to cents to avoid floating-point issues.
cents = round(amount * 100)

if cents == 0:
    print("No change")
else:
    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

if dollars > 0:
    if dollars == 1:
        print("1 Dollar")
    else:
        print(f"{dollars} Dollars")

if quarters > 0:
    if quarters == 1:
        print("1 Quarter")
    else:
        print(f"{quarters} Quarters")

if dimes > 0:
    if dimes == 1:
        print("1 Dime")
    else:
        print(f"{dimes} Dimes")

if nickels > 0:
    if nickels == 1:
        print("1 Nickel")
    else:
        print(f"{nickels} Nickels")

if pennies > 0:
    if pennies == 1:
        print("1 Penny")
    else:
        print(f"{pennies} Pennies")