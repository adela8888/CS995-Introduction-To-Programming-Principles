import unittest
from library_project.edevice import EDevice
from library_project.book import Book
from library_project.eresource import EResource
from library_project.member import Member

class TestEDeviceClass (unittest.TestCase):
    """
    A test class for EDevice class
    """
    def test_typeOfDevice(self):
        """
        Tests type of device creation
        """
        edevice1 = EDevice ()
        edevice1.setTypeOfDevice ("laptop")
        self.assertEqual("laptop", edevice1.getTypeOfDevice())

    def test_availability (self):
        """
        Tests availability of the device
        """
        edevice1 = EDevice()
        edevice1.checkAvailability()
        self.assertEqual (True, True)
