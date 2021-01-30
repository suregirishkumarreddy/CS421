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

# Create an empty list to hold the split quotes lines
quotes_lines_list_split = []

separator = ";"

# Split each quote with the Author into a sublist (using the separator - ;)
for quote_line in quotes_lines_list:
    quotes_lines_list_split.append(quote_line.split(separator))

# Sort the quote lines list by Author name
quotes_lines_list_split.sort(key = lambda quote_line : quote_line[1])

# Open the "quotes2.txt" file in Write-Text Mode
# Check the existence of "quotes2.txt" file. If exists, open in Append-Text Mode
if os.path.exists("quotes2.txt"):
    out_file2 = open("quotes2.txt","at")
else:
    out_file2 = open("quotes2.txt","wt")

# Join each quote line and author, with the separator in between
# Write the joined quote line into "quotes2.txt" file
for quote_line_split in quotes_lines_list_split:
    quote_line = separator.join(quote_line_split)
    out_file2.write(quote_line)

# Close Input and Output files
in_file.close()
out_file2.close()

