# Terrence Barnes Jr.
# 10/6/2026
# P2HW2
# This program collects six module grades and calculates the lowest grade, highest grade, sum, and average.

"""
Pseudocode:
1. Get the grade for Module 1.
2. Get the grade for Module 2.
3. Get the grade for Module 3.
4. Get the grade for Module 4.
5. Get the grade for Module 5.
6. Get the grade for Module 6.
7. Store all six grades in a list.
8. Find the lowest grade.
9. Find the highest grade.
10. Find the sum of all the grades.
11. Calculate the average of the grades.
12. Display the results.
"""

module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

grades = [module1, module2, module3, module4, module5, module6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum_of_grades / len(grades)

print()
print("------------Results------------")
print(f"{'Lowest Grade:':<20}{lowest_grade}")
print(f"{'Highest Grade:':<20}{highest_grade}")
print(f"{'Sum of Grades:':<20}{sum_of_grades}")
print(f"{'Average:':<20}{average_grade:.2f}")
print("--------------------------------")