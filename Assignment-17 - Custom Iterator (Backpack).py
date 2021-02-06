class Book:

    def __init__(self, name, isbn, author, year_of_release):
        self.name = name
        self.isbn = isbn
        self.author = author
        self.year_of_release = year_of_release

    def __repr__(self):
        return 'Name=%s, ISBN=%s, Author=%s, Year-of-Release=%s' % (self.name, self.isbn, self.author, self.year_of_release)

    def __str__(self):
        return 'Name=%s, ISBN=%s, Author=%s, Year-of-Release=%s' % (self.name, self.isbn, self.author, self.year_of_release)


class BackPack:

    def __init__(self, list_of_books):
        self.list_of_books = list_of_books

    def __repr__(self):
        return list_of_books.__str()

    def __str__(self):
        return list_of_books.__str()

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if (self.x < len(self.list_of_books)):
            current_book = self.list_of_books[self.x]
            self.x += 1
            return current_book
        else:
            raise StopIteration


    
# Creating an instance for each Book
book_1 = Book("Rich Dad Poor Dad", "978-1612680194", "Robert T. Kiyosaki", 1997)
book_2 = Book("How to Make Money in Stocks", "978-0071614139", "William J. O'Neil", 2009)
book_3 = Book("The Intelligent Investor", "978-0060555665", "Benjamin Graham", 1949)
book_4 = Book("Common Sense on Mutual Funds", "978-0470138137", "John Bogle", 1999)

# Create a list of Books
my_books = [book_1, book_2, book_3, book_4]


# Create an instance of BackPack with list of Books
my_backpack = BackPack(my_books)


for book in my_backpack:
    print(book)

