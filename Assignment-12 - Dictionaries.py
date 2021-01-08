# Sorts the Dictionary by the Keys  --> sorted(dict) returns the Keys of Dictionary in a sorted order
# Print the Keys (Candies) and corresponding value  --> To display the Dictionary, read through the Keys and print the Keys and corresponding value
def print_dictionary(input_dict):
    input_dict_keys_sorted = sorted(input_dict)
    for key in input_dict_keys_sorted:
        print(key + " = " + str(input_dict[key]))
        
# This function adds the values of two dictionaries
# Identify the unique list of Keys using LIST and SET functions
# Using the unique Keys identified, add the values of both dictionaries and result into one dictionary
def add_dictionaries(dict_1,dict_2):
    output_dict = {}
    dict_keys = set(list(dict_1.keys()) + (list(dict_2.keys())))
    for key in dict_keys:
        if (key in dict_1) and (key in dict_2):
            output_dict[key] = dict_1[key] + dict_2[key]
        elif key in dict_1:
            output_dict[key] = dict_1[key]
        else:
            output_dict[key] = dict_2[key]
    return output_dict
    
            
# List of Candies and corresponding Count in my Candy Bag
my_candy_bag = {    
   "snickers" : 5,
   "butterfinger" : 3,
   "candycorn" : 10,
   "skittles" : 6,
   "twix" : 7
}

# List of Candies and corresponding Count in my Brother's Bag
my_brothers_bag = {
   "starburst" : 5,
   "kitkat" : 6,
   "twix" : 8,
   "butterfinger" : 6,
   "candycorn" : 10
}

# Find all the Candies in our bags altogether and their corresponding total count of each candy
print("")
print("[1] Our Combined Bag:")
print("=====================")
our_combined_bag  = add_dictionaries(my_candy_bag, my_brothers_bag)
print_dictionary(our_combined_bag)



# Print my_candy_bag
print("")
print("[2] My Candy Bag:")
print("=====================")
print_dictionary(my_candy_bag)

# Print my_brothers_bag
print("")
print("[3] My Brother's Bag:")
print("=====================")
print_dictionary(my_brothers_bag)
