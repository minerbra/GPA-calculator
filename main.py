"""

@Author: Brady Miner

GPA Calculator: Will calculate n number of grades and return the average GPA.

"""

print("\nThis program will calculate your GPA based on the number of grades entered.\n"
      "Valid grades include '+' or '-' symbols.\n"
      "Invalid grades such as 'S' or 'G' will not be calculated.\n"
      "Type 'quit' to end the program and calculate GPA.")


grades = []  # List to store number of points associated with each grade
valid_grades = ''

valid = ("A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F")  # Stores valid grade entries
invalid = ''

while True:
    grade = input("\nEnter your grades (Ex. A+ A, A-): ").upper()  # Match user input to uppercase constraints

    points = 0

    if grade == "QUIT":  # If the user enters a blank line or types "quit" GPA is calculated
        break
    elif grade == '':
        break
    elif grade not in valid:  # Prevents invalid grades from being calculated into the GPA
        print("Grade is invalid, enter a valid grade")
        continue
    else:
        grade += valid_grades  # Add invalid inputs to separate list

    if grade == "A+":  # Accumulate the points for each grade inside the loop
        points = 4.2
    elif grade == "A":
        points = 4.0
    elif grade == "A-":
        points = 3.9
    elif grade == "B+":
        points = 3.7
    elif grade == "B":
        points = 3.2
    elif grade == "B-":
        points = 3.0
    elif grade == "C+":
        points = 2.8
    elif grade == "C":
        points = 2.2
    elif grade == "C-":
        points = 2.0
    elif grade == "D+":
        points = 1.8
    elif grade == "D":
        points = 1.2
    elif grade == "F":
        points = 0

    grades.append(points)

total = 0  # Store the total amount of GPA accumulated
num = 0  # Store the number of grades from user input


for grade in grades:  # Loop to increment the total grades
    total += grade
    num += 1

average = round(total / num, 3)  # Calculate the average GPA rounding to 3 decimal places

print("Your GPA is", average)  # Print the GPA and show the user
