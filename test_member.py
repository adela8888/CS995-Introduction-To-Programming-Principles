import unittest
from library_project.edevice import EDevice
from library_project.book import Book
from library_project.eresource import EResource
from library_project.member import Member

class TestMemberClass (unittest.TestCase):
    """
    A test class for the Member class
    """
    def test_studenNumber(self):
        """
        Tests creation of a student number
        """
        mem1 = Member()
        mem1.setStudentNumber ("0123")
        self.assertEqual ("0123",mem1.getStudentNumber())

    def test_addBookBorrowed(self):
        """
        Tests adding an object of a book to the list
        """
        book1= Book ()
        mem1 = Member()
        mem1.addBookBorrowed (book1)
        self.assertIn (book1, mem1.listOfBooksBorrowed)

    def test_addMessage (self):
        """
        Tests adding messages to the list of messages
        """
        mem1 = Member ()
        mem1.addMessage ("Hello")
        self.assertIn ("Hello", mem1.getAllMessages())

    def test_getNumberOfBooksBorrowed(self):
        """
        Tests number of books in the list
        """
        mem1 = Member ()
        self.assertEqual (0, mem1.getNumberOfBooksBorrowed())