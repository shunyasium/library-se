class LibraryError(Exception):
    pass


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise LibraryError("Duplicate Book ID")
        self.books[book_id] = {
            "title": title,
            "author": author,
            "borrowed": False
        }

    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise LibraryError("Book not found")
        if self.books[book_id]["borrowed"]:
            raise LibraryError("Book already borrowed")
        self.books[book_id]["borrowed"] = True

    def return_book(self, book_id):
        if book_id not in self.books:
            raise LibraryError("Book not found")
        self.books[book_id]["borrowed"] = False
