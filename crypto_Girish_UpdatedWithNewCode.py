#Program for generating the Crypto Quote

# Import String to generate Alphabet Characters
import string

# Import Random to shuffle the List
import random


#1. Class for representing a single QUOTE
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
   

#2. Class for representing all the quotes (quotes collection).
# This class represents a collection of quotes
# _repr__ and __str__
class QuotesList:

    # constructor method for creating a QuotesList object
    # The list of quotes should be constructed outside of the class
    def __init__(self, some_list_of_quotes):
        self.quotes_list = some_list_of_quotes
        

   
    # Another method for creating the  Quote object
    # This method takes the file name as the input
    # See https://stackoverflow.com/questions/44726196/how-to-implement-multiple-constructors-in-python
    @classmethod
    def createWithFileName(cls, file_name):
        # create an empty list of quotes
        quotes_list = [ ]

        # now process the file
        file = open(file_name)
        lines_list = file.readlines()
        for x in lines_list:
            fields = x.split(',')
            quote = Quote(fields[0], fields[1], fields[2], fields[3])
            #print(quote)
            quotes_list.append(quote)
        file.close()

        #print("printing the collection")
        #print(quotes_list_from_file)
        # now, return this 
        return cls(quotes_list)



    # We will now have a getMethod for other classes to get the quotes_list variable
    # from QuotesList object
    def getQuotesList(self):
         return self.quotes_list

    # This is a useful function to print the quotes_list
    # Can be called by different methods to validate that their methods are working
    def printQuotes(self):
        for x in self.quotes_list:
            print(x)
        


    # We will now have methods for __str, __ repr, and __ iter
    # these are the standard methods to print and iterate the object
    def __str__(self):
        return quotes_list.__str()

    def __repr__(self):
        return quotes_list.__str()

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if (self.x < len(self.quotes_list)):
            current_quote = self.quotes_list[self.x]
            self.x = self.x+1
            return current_quote
        else:
            raise StopIteration

    # For adding a quote to the collection
    def add(self, quote):
        self.quotes_list.append(quote)


# ========== Method No: 7: (Girish Kumar Sure) ========================

# Purpose: This method generate Crypto Quote for each input Quote and build a collection of Crypto Quotes
    def generateCryptoQuote(self, quote):
        upper_quote = quote.upper()
        quote_char_list = list(upper_quote)
        quote_char_list_temp = list(upper_quote)

        list_of_alphabets = []
        list_of_alphabets = list(string.ascii_uppercase)

        random_list_of_alphabets = list(list_of_alphabets)
        random.shuffle(random_list_of_alphabets)

        output_queue_pos = -1
        for quote_char in quote_char_list:
            output_queue_pos += 1
            if quote_char in list_of_alphabets:
                quote_char_alphbt_pos = list_of_alphabets.index(quote_char)
                replace_char = random_list_of_alphabets[quote_char_alphbt_pos]
                quote_char_list_temp[output_queue_pos] = replace_char

                cryptoquote = ''.join(quote_char_list_temp)

        return cryptoquote

# Purpose: This method builds a collection of Crypto Quotes for all the input Quotes
    def generateCryptoQuoteList(self):
        list_of_quotes = self.quotes_list
        cryptoquotes_list = []
        for quote_row in list_of_quotes:
            # list_of_quotes contains a list of Quotes Objects in it
            # Here quote_row is an Object that inherits the features of Quote Class
            quote_str = quote_row.quote
            cryptoquote = self.generateCryptoQuote(quote_str)
            cryptoquotes_list.append(cryptoquote)

        return cryptoquotes_list



class CryptoQuotesCollection(QuotesList):

    # Inheriting the constructors of QuotesList class
    # https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super/
    def __init__(self, list_of_quotes, list_of_cryptoquotes):
        QuotesList.list_of_quotes = list_of_quotes
        self.list_of_cryptoquotes = list_of_cryptoquotes

    def __repr__(self):
        return "ID: " + self.id + " Quote: " + self.quote + " Crypto Quote: " + self.cryptoquote + " Author: " + self.author + " Submitted by: " + self.submitted_by

    def __str__(self):
        return "ID: " + self.id + " Quote: " + self.quote + " Crypto Quote: " + self.cryptoquote + " Author: " + self.author + " Submitted by: " + self.submitted_by   
   

# Purpose: This method builds a collection of Quotes with corresponding Crypto Quote attached
    def buildCryptoQuoteCollection(self):
        list_of_quotes = QuotesList.list_of_quotes
        cryptoquote_collection = []
        pos = 0
        for quote_row in list_of_quotes:
            # list_of_quotes contains a list of Quotes Objects in it
            # Here quote_row is an Object that inherits the features of Quote Class
            self.id = quote_row.id
            self.quote = quote_row.quote
            self.author = quote_row.author
            self.submitted_by = quote_row.submitted_by
            self.cryptoquote = self.list_of_cryptoquotes[pos]
            pos += 1

    #hint_char = " + quote_list[0] + " = " + quote_list_temp[0])


#========================= STARTING POINT ==========================
# All the testing happens here
# Please ensure that you print some info about the method invocation and the results
# Please ensure that you put the method number, your name and method name in the print
#================= Starting Point ===============================
# This is the starting point for the program execution
#
# Step 1:  Create a QuotesList object from the input file
quotes_list_object = QuotesList.createWithFileName("quotes_in_excel.csv")



# ========= Girish Kumar Sure: Method # 7 ========================
# Generate Crypto Quote for each input quote and build a list of Crypto Quotes 
list_of_cryptoquotes = quotes_list_object.generateCryptoQuoteList()

# Create a CryptoQuotesCollection Object by passing QuotesList Object and List of Crypto Quotes
cryptoquotes_collection_object = CryptoQuotesCollection(quotes_list_object, list_of_cryptoquotes)

# Build a Collection of Quotes with the corresponding CryptoQuote attached
cryptoquotes_collection_object.buildCryptoQuoteCollection()

print(cryptoquotes_collection_object)




