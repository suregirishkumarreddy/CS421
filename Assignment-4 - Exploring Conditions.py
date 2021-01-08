# Get Day of the Week from User
day_of_week = input("Enter Day of the Week: ")

# Convert the Day of the Week to Uppercase
day_of_week = day_of_week.upper()

# Get the first 3 Characters of Day of the Week
day_of_week_3_chars = day_of_week[0:3]

# Print the Schedule of the Day, based on the Day of the Week entered
if day_of_week_3_chars == "SUN":
    print("1. Water the Garden and Lawn.")
    print("2. Go for Grocery Shopping.")
    print("3. Do the Lawn Mowing.")
elif day_of_week_3_chars == "MON":
    print("1. Start working of the coding of new program.")
elif day_of_week_3_chars == "TUE":
    print("1. Work on the coding of new program.")
    print("2. Review the SILC Python Class work.")
elif day_of_week_3_chars == "WED":
    print("1. Water the Lawn")
    print("2. Attend the Stand up meeting at 9 AM.")
    print("3. Complete the coding of new program.")
elif day_of_week_3_chars == "THU":
    print("1. Start the testing of the new program.")
    print("2. Go to Sai Baba Temple at 6 PM.")
elif day_of_week_3_chars == "FRI":
    print("1. Attend the Team Meeting at 9 AM.")
    print("2. Complete the testing of the new program.")
    print("3. Submit the SILC Python assignment before 12 AM.")
elif day_of_week_3_chars == "SAT":
    print("1. Attend the SILC Python Class at 11 AM.")
    print("2. Do the Laundry in the Afternoon.")
else:
    print("Error: Sorry. I don't understand what you are saying.")
