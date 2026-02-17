# Stage 3: Student Grade Calculator

name = input("Enter student name: ")

mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))

total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("\n", name)
print("Total:", total, "/300")
print("Percentage:", percentage, "%")
print("Grade:", grade)
