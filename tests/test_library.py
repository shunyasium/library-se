import unittest
from src.library import Library, LibraryError


class TestLibrarySprint1(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book_success(self):
        self.library.add_book("B1", "Python", "Guido")
        self.assertIn("B1", self.library.books)

    def test_add_duplicate_book(self):
        self.library.add_book("B1", "Python", "Guido")
        with self.assertRaises(LibraryError):
            self.library.add_book("B1", "Java", "James")


if __name__ == "__main__":
    unittest.main()
