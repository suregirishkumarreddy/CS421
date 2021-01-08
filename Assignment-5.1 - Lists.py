# Define Registered Students list
students = ["abe", "barb", "chris", "abe", "dan", "chris", "ellie", "peter"]

# Display the list of Students registered in the class
print("All students --> ", students)

# Define empty output unique Students list
student_temp = []

# Build the output list with unique list of Students in Class
for each_student in students:
    student_exists = False
    for each_unique_student in student_temp:
        if each_student == each_unique_student:
            student_exists = True
            
    if student_exists == False:
        student_temp.append(each_student)

# Move the unique list of Students to Student List
students = student_temp

# Display the Unique list of Students in Class
print("Unique students --> ", students)
