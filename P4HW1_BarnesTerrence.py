# Terrence Barnes Jr.
# 11/1/2026
# P4HW1
# This program collects test scores, calculates the average, and displays the letter grade

# Pseudocode:
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list to store the scores.
# 3. Use a loop to collect each score.
# 4. Check if each score is between 0 and 100.
# 5. If the score is invalid, ask the user to enter it again.
# 6. Add each valid score to the list.
# 7. Find and display the lowest score.
# 8. Remove the lowest score from the list.
# 9. Display the modified score list.
# 10. Calculate and display the average.
# 11. Determine and display the letter grade.

num_scores = int(input("How many scores do you want to enter? "))

scores = []

for i in range(num_scores):

    score = float(input(f"Enter score #{i + 1}: "))

    while score < 0 or score > 100:
        print("Invalid score!")
        print("Score should be between 0 and 100.")

        score = float(input(f"Enter score #{i + 1} again: "))

    scores.append(score)

lowest_score = min(scores)

print("\n----------Results----------")
print(f"Lowest score entered: {lowest_score}")

scores.remove(lowest_score)

print(f"Score List after dropping lowest score: {scores}")

average = sum(scores) / len(scores)

print(f"Average: {average:.2f}")

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")