import json

# Custom Exceptions
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def __repr__(self):
        return f"Book({self.title}, {self.author}, Borrowed: {self.is_borrowed})"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)
        return f"{self.name} borrowed {book.title}."
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            return f"{self.name} returned {book.title}."
        return f"{self.name} did not borrow {book.title}."
    
    def __repr__(self):
        return f"Member({self.name}, Borrowed Books: {[book.title for book in self.borrowed_books]})"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    
    def add_book(self, title, author):
        self.books[title] = Book(title, author)
        return f"Book '{title}' added to the library."
    
    def add_member(self, name):
        self.members[name] = Member(name)
        return f"Member '{name}' added to the library."
    
    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException("Book not found in the library.")
        if member_name not in self.members:
            return "Member not registered."
        return self.members[member_name].borrow_book(self.books[book_title])
    
    def return_book(self, member_name, book_title):
        if member_name not in self.members:
            return "Member not registered."
        if book_title not in self.books:
            return "Book not found in the library."
        return self.members[member_name].return_book(self.books[book_title])
    
# Example Usage
library = Library()
print(library.add_book("1984", "George Orwell"))
print(library.add_member("Alice"))
print(library.borrow_book("Alice", "1984"))
print(library.return_book("Alice", "1984"))
