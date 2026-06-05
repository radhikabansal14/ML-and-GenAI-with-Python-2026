#Create a Student Report Program that take student details using input(), Store marks in variables, Calculate total and percentage , Use comments, Use proper indentation
# Taking student details as input
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks of 3 subjects
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

# Calculating total marks
total = maths + science + english

# Calculating percentage
percentage = (total / 300) * 100

# Displaying student report
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("Maths Marks:", maths)
print("Science Marks:", science)
print("English Marks:", english)
print("Total Marks:", total)
print("Percentage:", percentage, "%")