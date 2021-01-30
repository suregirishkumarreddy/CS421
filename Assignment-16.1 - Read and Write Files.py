# From the current working directory (cwd), open the "quotes.txt" file in Read-Text Mode
# First check for the existence of file "quotes.txt"
import os
if os.path.exists("quotes.txt"):
    in_file = open("quotes.txt", "rt")
else:
    print("quotes.txt does not exist")
    exit()

# Read all the lines of file into a list
quotes_lines_list = in_file.readlines()

# Sort the list of lines
quotes_lines_list.sort()

# Open the "quotes1.txt" file in Write-Text Mode
# Check the existence of "quotes1.txt" file. If exists, open in Append-Text Mode
if os.path.exists("quotes1.txt"):
    out_file1 = open("quotes1.txt","at")
else:
    out_file1 = open("quotes1.txt","wt")

# Write each quote line into "quotes1.txt" file
for quote_line in quotes_lines_list:
    out_file1.write(quote_line)

# Close Input and Output files
in_file.close()
out_file1.close()
