# Define a list (html) with list of all students attending html class
html = [ "guy", "madeline", "parker", "chris", "tom", "ursula", "ramesh", 
"lisa", "staci", "jordan", "emmett", "vinny", "brian", "zora", "oliver", 
"polly", "kingston", "olivia", "xavier", "fiona", "zack", "harmony", 
"barb", "samson", "ariel", "emma", "yasmine", "crystal", "dan", "xenia", 
"irving", "tiffany", "noah", "umesh", "yates", "victoria", "desiree", 
"quinn", "wendy", "frank", "henry", "mike", "isabella", "nora", "julie", 
"lincoln", "alex", "kim", "raven", "watson", "ganga"]

# Define empty lits (html_a, html_b)
html_a = [] 
html_b = []

# Group the list of Students with their first letter being
#       "a" to "m" into html_a
#       "n" to "z" into html_b

for each_student in html:
    if each_student < "n":
        html_a.append(each_student)
    else:
        html_b.append(each_student)

# Sort the html list in the alphabetical order
html.sort()

# Sort the html_a list in the alphabetical order
html_a.sort()

# Sort the html_b list in the alphabetical order
html_b.sort()

# Print the List of Students in the Class - All Students, "a" to "m" and "n" to "z"
print("List of All Students in Class: ", html)
print("List of first group of Students ("a" to "m"): ", html_a)
print("List of Second group of Students ("n" to "z"): ", html_b)
