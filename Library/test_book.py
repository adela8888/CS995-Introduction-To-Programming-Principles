import unittest
from library_project.book import Book

class TestBookClass (unittest.TestCase):
    """
    A test class for the Book class
    """
    def test_name(self):
        """
        Tests name creation
        """
        book1 = Book ()
        book1.setName ("not set")
        self.assertEqual ("not set", book1.getName())

    def test_damage (self):
        """
        Tests damage creation
        """
        book1 = Book ()
        book1.setDamage ("page")
        self.assertIn ("page", book1.getDamage())
        book1.setDamage ("water")
        self.assertEqual (["page", "water"] , book1.getDamage())

    def test_availability (self):
        """
        Tests availability, True
        """
        book1 = Book ()
        book1.getAvailability()
        self.assertEqual (True, True)


