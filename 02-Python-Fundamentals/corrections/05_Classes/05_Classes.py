# 1. Create a Book Class
# Define a class named Book.
# The Book class should have an __init__() method that takes parameters for the book’s name, author, and release_date.
# Store these parameters as attributes of the instance.
# Optionally, include a boolean attribute read initialized to False to track if the book has been read.
class Book:
    def __init__(self, name, author, release_date):
        self.name = name;
        self.author = author;
        self.release_date = release_date;
    def __str__(self):
        return f"Title: {self.name}\nAuthor: {self.author}\nRelease year: {self.release_date}"


# 2. Create a BookCollection Class
# Define a class named BookCollection.
# In the __init__() method, initialize the books to a list of books passed to the
# constructor or an empty list.
# If you pass a list, verify its elements are indeed instances of a Book otherwise, 
# raise and exception.
class BookCollection:
    def __init__(self, books=None):
        if books == None:
            books = [];
        if not all(isinstance(book, Book) for book in books):
            raise TypeError("All elements must be instances of Book.")
        self.books = books;

# 3. Add Books to the Collection
# Within the BookCollection class, create a method add_book(self, book) that takes a Book
# object as a parameter and adds it to the collection (self.books).
# Verify every new entry is indeed an instance of Book otherwise, raise and exception.
    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added.");
        self.books.append(book);

# 4. Mark Books as Read
# In the BookCollection class, implement a method mark_as_read(self, book_name) that:
# Searches for a book by its name in the collection.
# If found, sets its read attribute to True.
# If not found, optionally prints a message indicating the book isn’t in the collection.
    def mark_as_read(self, book_name):
        for book in self.books:
            if book.name == book_name:
                book.read = True
                return
        print(f"Book '{book_name}' not found in the collection")

    def mark_as_unread(self, book_name):
        for book in self.books:
            if book.name == book_name:
                book.read = False
                return
        print(f"Book '{book_name}' not found in the collection")
            
# 5. Display Collection Status
# Optionally, add a method list_books(self) in BookCollection that prints out all the books 
# with their details and read status.
    def list_books(self):
        for book in self.books:
            if hasattr(book, "read"):
                status = "Read" if book.read else "Unread";
            else:
                status = "Unkown"
            print(f"Title: {book.name}\nAuthor: {book.author}\nRelease year: {book.release_date}\nStatus: {status}\n")


new_book_collection = BookCollection();
print(new_book_collection)



new_book_collection.add_book(Book("Harry Potter", "J.K. Rowling", 1998));
new_book_collection.add_book(Book("Bible", "Unkown", -1000));
new_book_collection.add_book(Book("The Hobbit", "J.R.R. Tolkien", 1937));

new_book_collection.mark_as_read("Harry Potter");
new_book_collection.mark_as_unread("Bible");

new_book_collection.list_books()