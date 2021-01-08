# In this function the input word is reveresed to check if it is a Palindrome word
def isPalindrome(word):
    word = word.lower()
    word_reverse = ""

    for char in word:
        word_reverse = char + word_reverse

    if word == word_reverse:
        return "True"
    else:
        return "False"

# Get the word from User to check for Palindrome word
input_word = input("Enter a word to check for Palindrome: ")

# Display if the input word is Palindrome or not
print("Is the input word '" + input_word + "' a Palindrome: " + isPalindrome(input_word))
