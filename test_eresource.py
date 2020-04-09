import unittest
from library_project.edevice import EDevice
from library_project.book import Book
from library_project.eresource import EResource
from library_project.member import Member

class TestEResourceClass (unittest.TestCase):
    """
    A test class for EResource class
    """
    def test_setYearOfPublication (self):
        """
        Tests year of publication creation
        """
        er1 = EResource()
        er1.setYearOfPublication (0)
        self.assertEqual (0,0)

    def test_addDevice (self):
        """
        Tests adding a new object to the list
        """
        d = EDevice()
        er1 = EResource()
        er1.addDevice (d)
        self.assertIn (d, er1.devices)

    def test_setMember(self):
        """
        Tests member creation
        """
        m = Member()
        er1=EResource()
        er1.setMember (m)
        self.assertEqual (m, er1.getMember())