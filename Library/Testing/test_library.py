import unittest
from library_project.edevice import EDevice
from library_project.book import Book
from library_project.eresource import EResource
from library_project.member import Member
from library_project.library import Library

class TestLibraryClass (unittest.TestCase):
    """
    A test class for the Library class
    """
    def test_setLocation(self):
        """
        Tests location creation
        """
        lib1 = Library()
        lib1.setLocation("Glasgow")
        self.assertEqual ("Glasgow", lib1.getLocation())

    def test_ListOfResources(self):
        """
        Tests adding resources objects to the list of resources
        """
        book1 = Book ()
        lib1 = Library()
        lib1.addResource (book1)
        self.assertIn (book1, lib1.listOfResources)

    def test_getListofMembers (self):
        """
        Tests list of members
        """
        lib1 = Library ()
        self.assertEqual (0, len(lib1.listOfMember))


"""
Conventional testing

lib1 = Library()
book1 = Book ()
book2 = Book ()
ebook1 = EResource ()
lib1.addResource(book2)
lib1.addResource(book1)
lib1.addResource(ebook1)
mem1 = Member ()
lib1.lendResource(book1, mem1)
lib1.returnResource(book1, mem1, damage = True, damageRecord="cover destroyed")
mem1.addBookBorrowed(book2)
lib1.lendResource(book2, mem1)
lib1.sendMessage("You cannot return any books this Friday due to closure")
print (mem1.getAllMessages())

print ("===============================")
lib1.printEveryBooklDetails()

print ("===============================")
book3 = Book()
mem1 = Member()
lib1.setName("Strath Library")
lib1.setLocation("Glasgow")
lib1.addResource(book3)
lib.checkResourseExists(book1)
"""


