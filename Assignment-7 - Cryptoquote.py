# Import String to generate Alphabet Characters
import string

# Import Random to shuffle the List
import random

# Get the quote from User
quote = input("Enter a quotation: ")

# Convert the quote into Uppercase
upper_quote = quote.upper()

# Breakdown the quote into a list of characters
quote_list = list(upper_quote)

# Hold the List of characters of quote in a Temp variable
quote_list_temp = list(upper_quote)

# Create an empty list to hold alphabets
list_of_alphabets = []

# Using String functions, create the list of alphabets in Uppercase
list_of_alphabets = list(string.ascii_uppercase)

# Copy the Alphabet list to shuffle the Alphabet Characters
random_list_of_alphabets = list(list_of_alphabets)

# Shuffle the list of Alphabets using Random module
random.shuffle(random_list_of_alphabets)

# Default the Queue Position for Output Cryptoquote list
output_queue_pos = -1

# Find the alphabet position of a character
# Identify the replacement character from the Random list of alphabets
# Replace the character from random list into the Temp variable to build cryptoquote
for quote_char in quote_list:
    output_queue_pos += 1
    if quote_char in list_of_alphabets:
        quote_char_alphbt_pos = list_of_alphabets.index(quote_char)
        replace_char = random_list_of_alphabets[quote_char_alphbt_pos]
        quote_list_temp[output_queue_pos] = replace_char

# Finally join all the list of crypto characters to make a cryptoquote
cryptoquote = ''.join(quote_list_temp)

# Display the User Input Quote
print("Input Quote: ", quote)

# Display the converted Crypto Quote
print("Crypto Quote: ", cryptoquote)

# Display a Hint of conversion used in generating Crypto Quote
print("Hint: " + quote_list[0] + " = " + quote_list_temp[0])
