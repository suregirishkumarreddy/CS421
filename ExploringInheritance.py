#Program for generating the Crypto Quote

# Import String to generate Alphabet Characters
import string

# Import Random to shuffle the List
import random


#======= Class Quote =============================
# Class for representing a single QUOTE
# id, quote, author, submitted_by
# _repr__ and __str__
class Quote:
    
    def __init__(self, id, quote, author, submitted_by):
        self.id = id
        self.quote = quote
        self.author = author
        self.submitted_by = submitted_by

    def __repr__(self):
        return "ID: " + self.id + " Quote: " + self.quote + " Author: " + self.author + " Submitted by: " + self.submitted_by

    def __str__(self):
        return "ID: " + self.id + " Quote: " + self.quote + " Author: " + self.author + " Submitted by: " + self.submitted_by    
   

#======= Class Crypto =============================
# Class for representing a single Quote with Crypto Parameters
# Class Crypto inherits the features of Class Quote and new attributes specific to Crypto Class
# Quote Class attributes (id, quote, author, submitted_by), crypto_quote and hint
# _repr__ and __str__
class Crypto(Quote):
    
    def __init__(self, id, quote, author, submitted_by, crypto_quote, hint):
        super().__init__(id, quote, author, submitted_by)
        self.crypto_quote = crypto_quote
        self.hint = hint

    def __repr__(self):
        return "ID: " + self.id + " Quote: " + self.quote + " Author: " + self.author + " Submitted by: " + self.submitted_by + " CryptoQuote: " + self.crypto_quote + " Hint: " + self.hint

    def __str__(self):
        return "ID: " + self.id + " Quote: " + self.quote + " Author: " + self.author + " Submitted by: " + self.submitted_by + " CryptoQuote: " + self.crypto_quote + " Hint: " + self.hint
        
    def generateCrypto(self):
        return "To Be Implemented"

    def generateHint(self):
        return "To Be Implemented"
    

# 2 intances of Crypto Class with all attributes
cryptoquote_1 = Crypto("1", "First", "Author-1", "SubmittedBy-1", "Crypto-1", "Hint-1")
cryptoquote_2 = Crypto("2", "Second", "Author-2", "SubmittedBy-2", "Crypto-2", "Hint-2")

print(cryptoquote_1)
print(cryptoquote_2)
