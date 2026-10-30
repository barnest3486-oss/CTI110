# Terrence Barnes Jr.
# P4LAB2
# 10/30/2026
# Program uses loops to display multiplication tables to users

# Pseudocode:
# 1. Start the program.
# 2. Ask the user to enter an integer.
# 3. If the number is 0 or greater:
#       Display the multiplication table from 1 to 12.
# 4. Otherwise:
#       Display a message that negative values are not accepted.
# 5. Ask the user if they want to run the program again.
# 6. If the user enters yes, repeat the program.
# 7. If the user enters no, end the program.

run_again = "yes"

while run_again == "yes":

    number = int(input("Enter an integer: "))

    if number >= 0:
        print(f"Multiplication table for {number}:")

        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")

    else:
        print("Negative values are not accepted.")

    run_again = input("Would you like to run the program again? (yes/no): ").lower()

print("Program ended.")
