# Terrence Barnes Jr.
# 10/6/2026
# P2HW1
# This program calculates and displays travel expenses.

print("This program calculates and displays travel expenses")

budget = float(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print("\n" + "-" * 40 + "Travel Expenses" + "-" * 40)

print(f"{'Location:':<20}{destination:>20}")
print(f"{'Initial Budget:':<20}${budget:>19.2f}")
print(f"{'Fuel:':<20}${gas:>19.2f}")
print(f"{'Accomodation:':<20}${accommodation:>19.2f}")
print(f"{'Food:':<20}${food:>19.2f}")

print("-" * 80)

print(f"\n{'Remaining Balance:':<20}${remaining_balance:>19.2f}")