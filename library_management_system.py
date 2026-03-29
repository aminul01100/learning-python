"""
project two
business: Library Management system
functionalities:
    1. add a book
    2. update a book
    3. view list of the books
    4. borrow a book
    5. return the borrowed book
    6. view list of the borrowed books
"""

import inspect
from abc import abstractmethod

# new_class = type(Book, (), {"__init__": lambda self, book_id, name, author: setattr(self, "id", book_id) or setattr(self, "book_name", name) or setattr(self, "author", author) or setattr(self, "is_borrowed", False) or setattr(self, "borrowed_by", None), "__str__": lambda self: f"Book(id={self.id}, title={self.book_name}, author={self.author}, is_borrowed={self.is_borrowed})"})
class CustomMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name.__contains__("_"):
            raise ValueError("Class name should not contain underscores.")
        return super().__new__(cls, name, bases, attrs)

class CustomMetaClassVersion2(CustomMetaClass):
    def __new__(cls, name, bases, attrs):
        init_method = attrs.get("__init__")
        method_body = inspect.getsource(init_method)
        method_definition_line = method_body.split(":")[0]
        attribute_str = method_definition_line.split("self, ")[1]
        attribute_list = attribute_str.split(", ")
        if len(attribute_list) > 5:
            raise ValueError("Number of attributes in __init__ method should not exceed 5.")
        # print(attribute_str)
        return super().__new__(cls, name, bases, attrs)

class BookNew(metaclass=CustomMetaClass):
    def __init__(self, book_id, name, author):
        self.id = book_id
        self.book_name = name
        self.author = author
        self.is_borrowed = False
        self.borrowed_by = None


class Book(metaclass=CustomMetaClass):
    def __init__(self, book_id, name, author, stored_at=None):
        self.id = book_id
        self.book_name = name
        self.author = author
        self.stored_at = stored_at

        self.is_borrowed = False
        self.borrowed_by = None

    @abstractmethod
    def borrow_book(self, borrower_name):
        pass

    def __str__(self):
        return f"Book(id={self.id}, title={self.book_name}, author={self.author}, is_borrowed={self.is_borrowed})"

class PdfBook(Book):
    def __init__(self, book_id, name, author, stored_at=None, file_size=None):
        super().__init__(book_id, name, author, stored_at)
        self.type = "pdf"

    def borrow_book(self, borrower_name):
        if self.is_borrowed:
            print(f"Sorry, the book '{self.book_name}' is already borrowed by {self.borrowed_by}.")
        else:
            self.is_borrowed = True
            self.borrowed_by = borrower_name
            # sending email to the borrower with the download link of the book
            print(f"You have successfully borrowed the book '{self.book_name}'.")
    
class PhysicalBook(Book):
    def __init__(self, book_id, name, author, stored_at=None, weight=None):
        super().__init__(book_id, name, author, stored_at)
        self.type = "physical"

    def borrow_book(self, borrower_name):
        if self.is_borrowed:
            print(f"Sorry, the book '{self.book_name}' is already borrowed by {self.borrowed_by}.")
        else:
            self.is_borrowed = True
            self.borrowed_by = borrower_name
            # placing an order of the book from the storage
            print(f"You have successfully borrowed the book '{self.book_name}'.")

class ComicBook(Book):
    def __init__(self, book_id, name, author, stored_at=None, illustrator=None):
        super().__init__(book_id, name, author, stored_at)
        self.type = "comic"

    def borrow_book(self, borrower_name):
        if self.is_borrowed:
            print(f"Sorry, the book '{self.book_name}' is already borrowed by {self.borrowed_by}.")
        else:
            self.is_borrowed = True
            self.borrowed_by = borrower_name
            # placing an order of the book from the storage
            print(f"You have successfully borrowed the book '{self.book_name}'.")

class BookManager:
    def __init__(self):
        self.number_of_books = 0
        self.books = dict() # book_id -> book_object

    def __str__(self):
        return f"BookManager(number_of_books={self.number_of_books})"
    
    # 1. add a book
    def add_book(self, name, author):
        new_book_id = self.number_of_books + 1
        # take user input to decide which class to use while creating a book object accordingly
        book = PdfBook(new_book_id, name, author)
        self.books[new_book_id] = book
        self.number_of_books += 1
        print(f"Book added successfully: {book}")

    # 2. update a book
    def update_book(self, book_id, new_name=None, new_author=None):
        if not new_name and not new_author:
            print("No new details provided for update.")
            return
        
        if book_id in self.books:
            book = self.books[book_id]
            if new_name:
                book.book_name = new_name
            if new_author:
                book.author = new_author
            print(f"Book updated successfully: {book}")

    # 3. view list of the books
    def view_book_list(self):
        print("List of books in the library:")
        for book_id, book in self.books.items():
            print(book)

    # 4. borrow a book
    def borrow_book(self, book_id, borrower_name):
        if book_id in self.books:
            book = self.books[book_id]
            book.borrow_book(borrower_name)


# book_manager = BookManager()

# book_manager.add_book("The Great Gatsby", "F. Scott Fitzgerald")
# book_manager.add_book("To Kill a Mockingbird", "Harper Lee")
# book_manager.add_book("1984", "George Orwell")

# book_manager.view_book_list()

a_random_list = [1, 2, 3, 4, 5]
print(type(a_random_list))