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

class Book:
    def __init__(self, book_id, name, author, stored_at=None):
        self.id = book_id
        self.book_name = name
        self.author = author
        self.stored_at = stored_at

        self.is_borrowed = False
        self.borrowed_by = None
        

    def __str__(self):
        return f"Book(id={self.id}, title={self.book_name}, author={self.author}, is_borrowed={self.is_borrowed})"

class BookManager:
    def __init__(self):
        self.number_of_books = 0
        self.books = dict() # book_id -> book_object

    def __str__(self):
        return f"BookManager(number_of_books={self.number_of_books})"
    
    # 1. add a book
    def add_book(self, name, author):
        new_book_id = self.number_of_books + 1
        book = Book(new_book_id, name, author)
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


book_manager = BookManager()

book_manager.add_book("The Great Gatsby", "F. Scott Fitzgerald")
book_manager.add_book("To Kill a Mockingbird", "Harper Lee")
book_manager.add_book("1984", "George Orwell")

book_manager.view_book_list()