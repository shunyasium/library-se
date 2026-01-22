import unittest
from src.library import Library, LibraryError


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    # ---------- Sprint 1 ----------
    def test_add_book_success(self):
        self.library.add_book("B1", "Python", "Guido")
        self.assertIn("B1", self.library.books)

    def test_add_duplicate_book(self):
        self.library.add_book("B1", "Python", "Guido")
        with self.assertRaises(LibraryError):
            self.library.add_book("B1", "Java", "James")

    # ---------- Sprint 2 ----------
    def test_borrow_available_book(self):
        self.library.add_book("B1", "Python", "Guido")
        self.library.borrow_book("B1")
        self.assertTrue(self.library.books["B1"]["borrowed"])

    def test_borrow_unavailable_book(self):
        self.library.add_book("B1", "Python", "Guido")
        self.library.borrow_book("B1")
        with self.assertRaises(LibraryError):
            self.library.borrow_book("B1")

    def test_return_book(self):
        self.library.add_book("B1", "Python", "Guido")
        self.library.borrow_book("B1")
        self.library.return_book("B1")
        self.assertFalse(self.library.books["B1"]["borrowed"])

    # ---------- Sprint 3 ----------
    def test_report_header(self):
        report = self.library.generate_report()
        self.assertIn("Book ID | Title | Author | Status", report)

    def test_report_contains_book(self):
        self.library.add_book("B1", "Python", "Guido")
        report = self.library.generate_report()
        self.assertIn("B1 | Python | Guido | Available", report)


if __name__ == "__main__":
    unittest.main()
