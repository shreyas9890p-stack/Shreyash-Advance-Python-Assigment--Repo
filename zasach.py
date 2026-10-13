"""# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


# Patron Class
class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    # Add a new book
    def add_book(self, book):
        self.books.append(book)
        print(f'"{book.title}" added to the library.')

    # Register a new patron
    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f'{patron.name} registered successfully.')

    # Borrow a book
    def borrow_book(self, patron_name, book_title):
        patron = None
        book = None

        for p in self.patrons:
            if p.name == patron_name:
                patron = p
                break

        for b in self.books:
            if b.title == book_title:
                book = b
                break

        if patron and book:
            if book.available:
                book.available = False
                patron.borrowed_books.append(book)
                print(f'{patron.name} borrowed "{book.title}".')
            else:
                print(f'"{book.title}" is not available.')
        else:
            print("Book or Patron not found.")

    # Return a book
    def return_book(self, patron_name, book_title):
        patron = None

        for p in self.patrons:
            if p.name == patron_name:
                patron = p
                break

        if patron:
            for book in patron.borrowed_books:
                if book.title == book_title:
                    book.available = True
                    patron.borrowed_books.remove(book)
                    print(f'{patron.name} returned "{book.title}".')
                    return

        print("Return operation failed.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f"{book.title} by {book.author} - {status}")


# ---------------- Main Program ----------------

library = Library()

# Add Books
library.add_book(Book("Python Programming", "Guido"))
library.add_book(Book("Data Structures", "Mark"))
library.add_book(Book("Machine Learning", "Andrew"))

# Register Patrons
library.register_patron(Patron("Raj"))
library.register_patron(Patron("Aman"))

# Display Books
library.display_books()

# Borrow Book
library.borrow_book("Raj", "Python Programming")

# Display Books
library.display_books()

# Return Book
library.return_book("Raj", "Python Programming")

# Display Books
library.display_books()"""



