# Define Students list registered for html and python class
html = [ "barb", "dan", "ellie", "abe", "chris"]
python = ["henry", "chris", "dan", "ellie", "frank", "gavin"]

# Define empty Students list registered for both classes
dupe_list = []

# Find the students registered both in html and python classes
for html_student in html:
    for python_student in python:
        if python_student == html_student:
            dupe_list.append(python_student)

# Display the list of Students registered for html, python and both classes
print("html students --> ", html)
print("python students --> ", python)
print("students registered in both html and python classes --> ", dupe_list)
