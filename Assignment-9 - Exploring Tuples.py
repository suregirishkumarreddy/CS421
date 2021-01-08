# This function calculates the Average Age of all Students in the Class
def getAverageAge(students_tuple):
    total_age = 0
    for each_student in students_tuple:
        name, age, marks = each_student
        total_age += age
    
    total_no_of_students = len(students_tuple)
    average_age = total_age / total_no_of_students
    
    return average_age

# This function calculates the Average Marks of all Students in the Class
def getAverageMarks(students_tuple):
    total_marks = 0
    for each_student in students_tuple:
        name, age, marks = each_student
        total_marks += marks
    
    total_no_of_students = len(students_tuple)
    average_marks = total_marks / total_no_of_students
    
    return average_marks

# This function finds the Highest Mark in the Class
def getHighestMark(students_tuple):
    highest_mark = 0
    for each_student in students_tuple:
        name, age, marks = each_student
        if marks > highest_mark:
            highest_mark = marks
    
    return highest_mark

# This function finds the Lowest Mark in the Class
def getLowestMark(students_tuple):
    lowest_mark = 100
    for each_student in students_tuple:
        name, age, marks = each_student
        if marks < lowest_mark:
            lowest_mark = marks
    
    return lowest_mark

# This function builds a summary of students info by calling individual functions
def getSummary(students_tuple):
    total_no_of_students = len(students_tuple)
    average_age = getAverageAge(students_tuple)
    average_marks = getAverageMarks(students_tuple)
    highest_mark = getHighestMark(students_tuple)
    lowest_mark = getLowestMark(students_tuple)
   
    students_summary = (total_no_of_students, average_age, average_marks, highest_mark, lowest_mark)
   
    return students_summary

# Student details of the PHP class
student_1 = ("abe", 16, 88)
student_2 = ("barb", 30, 72)
student_3 = ("chris", 14, 92)
student_4 = ("dan", 20, 80)
student_5 = ("ethan", 16, 60)

# A tuple of all student details in the PHP class
php_class = (student_1, student_2, student_3, student_4, student_5)

# Get a summary of student details
summary_tuple = getSummary(php_class)

total_no_of_students, average_age, average_marks, highest_mark, lowest_mark = summary_tuple

print("total no of students = ", total_no_of_students)
print("average age = ",average_age)
print("average marks = ",average_marks)
print("highest mark = ",highest_mark)
print("lowest mark = ", lowest_mark)
