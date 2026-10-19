# Terrence Barnes Jr.
# 10/18/2026
# P3HW1
# This program collects six module grades, calculates grade statistics, and displays the letter grade based on the average.
#
# Pseudocode:
# Ask the user to enter grades for six modules.
# Store the six grades in a list.
# Find the lowest grade, highest grade, and sum of the grades.
# Calculate the average of the six grades.
# Use the average to determine the letter grade.
# Display the lowest grade, highest grade, sum, average, and letter grade.

# Enter grades for six modules
mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
grade_sum = sum(grades)
avg = grade_sum / len(grades)

# Display grade statistics
print()
print("------------Results------------")
print(f"Lowest Grade:   {low:g}")
print(f"Highest Grade:  {high:g}")
print(f"Sum of Grades:  {grade_sum:g}")
print(f"Average:        {avg:.2f}")

# Determine letter grade for average
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Your grade is: {letter_grade}")
print("--------------------------------")