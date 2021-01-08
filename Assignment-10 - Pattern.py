# This Function displays the Input Character in a Pattern requested
def pattern(input_char = "*", line_count = 5, display_mode = "RIGHT"):
    
    display_mode = display_mode.upper()
    for i in range(line_count):
        # Calculate the no of Spaces to display based on the display mode
        if display_mode == "LEFT":
            no_of_spaces = 0
        elif display_mode == "CENTER":
            no_of_spaces = (line_count-i-1)
        elif display_mode == "RIGHT":
            no_of_spaces = (2*(line_count-i-1))
        else:
            print("Invalid Display Mode")
        
        # Calculate the no of Characters to display
        no_of_input_char = (2*i) + 1
        print((" " * no_of_spaces) + (input_char * no_of_input_char))

print('Test Case 1:  pattern("*",5,"RIGHT")')
pattern("*",5,"RIGHT")

print('Test Case 2:  pattern("@",6,"LEFT")')
pattern("@",6,"LEFT")

print('Test Case 3:  pattern("#",10,"CENTER")')
pattern("#",10,"CENTER")

print('Test Case 4: pattern()')
pattern( )

print('Test Case 4: pattern("X", 5)')
pattern("X",5)

print('Test Cae 5: With User Input')
display_char = input("Enter the Character to Display: ")
no_of_lines = int(input("How many lines do you need: "))
display_pattern = input("How do you want to justify the display (LEFT, RIGHT, CENTER): ")
pattern(display_char, no_of_lines, display_pattern)
