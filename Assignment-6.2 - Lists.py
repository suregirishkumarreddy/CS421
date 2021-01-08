# Define List of Students attending Python Class
python = ["abe", "barb", "chris", "dan", "ellie", "gabby", "henry", "isabelle", "jack", "larry"]

# Define the attendance list, with students attended in the last 4 weeks
week_1  = ["barb", "chris", "dan", "ellie", "henry", "isabelle", "jack"]
week_2  = ["abe", "barb", "chris",  "ellie", "gabby", "henry", "isabelle",  "larry"]
week_3  = ["abe", "barb",  "henry", "isabelle", "jack", "larry"]
week_4  = ["abe", "barb", "chris", "dan", "ellie", "gabby", "henry", "isabelle", "jack"]

# Define the list to hold the attendance
attendance_report = []

# Find the presence of each student of python class in each week
# Build the attendance report of each student
for each_student in python:
    student_attendance = []
    student_attendance.append(each_student)
    
    if each_student in week_1:
        student_attendance.append('P')
    else:
        student_attendance.append('A')
  
    if each_student in week_2:
        student_attendance.append('P')
    else:
        student_attendance.append('A')
    
    if each_student in week_3:
        student_attendance.append('P')
    else:
        student_attendance.append('A')

    if each_student in week_4:
        student_attendance.append('P')
    else:
        student_attendance.append('A')   
    attendance_report.append(student_attendance)

# Print the attendance report of each student of Python class
for each_student_attendance in attendance_report:
    print(*each_student_attendance)
