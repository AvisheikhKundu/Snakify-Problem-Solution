# Read the number of students and apples from the user input
students = int(input("Enter the number of students: "))
apples = int(input("Enter the number of apples: "))

# Calculate how many apples each student will get
apples_per_student = apples // students

# Calculate how many apples will remain
apples_remainder = apples % students

# Print the result
print(apples_per_student)
print(apples_remainder)
