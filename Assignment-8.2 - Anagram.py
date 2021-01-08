# This function checks if the input words are Anagrams
def areAnagrams(word_1,word_2):
    word_1 = word_1.lower().replace(" ","")
    word_2 = word_2.lower().replace(" ","")

    word_1_list = list(word_1)
    word_1_list.sort()   

    word_2_list = list(word_2)
    word_2_list.sort()

    if word_1_list == word_2_list:
        return "True"
    else:
        return "False"

# Get the word_1 and word_2 from User to check for Anagram word
print("Enter the words to check for Anagram")
input_word_1 = input("First word: ")
input_word_2 = input("Second word: ")

# Display if the input words are Anagrams or not
print("Are the input words '" + input_word_1 + "' and '" + input_word_2 + "' Anagrams: " + areAnagrams(input_word_1,input_word_2))
