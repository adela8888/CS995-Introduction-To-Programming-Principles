class EDevice:
    """
    A class to represent a real-life object with its parameters. In this case
    to represent an electronic device
    """

    def __init__(self, member = None):
        """
        A constructor to initialize the instance members of the class EDevice
        """
        self.typeOfDevice = "not set"
        self.IPAddress = "not set"
        self.location = "not set"
        self.availability = True
        self.loggedInMember = member

    def setTypeOfDevice (self, n):
        """
        Sets type of an electronic device
        """
        self.typeOfDevice = n

    def getTypeOfDevice (self):
        """
        Returns type of an electronic device
        """
        return self.typeOfDevice

    def setIPAddresss(self, i):
        """
        Sets IP address of an electronic device
        """
        self.IPAddress = i

    def getIPAddress(self):
        """
        Returns IP address of an electronic device
        """
        return self.IPAddress

    def setLocation(self, l):
        """
        Sets location of an electronic device in the library
        """
        self.location = l

    def getLocation (self):
        """
        Returns location of an electronic device in the library
        """
        return self.location

    def checkAvailability (self):
        """
        Checks if an electronic device is available
        """
        if self.loggedInMember is None:
            return True
        return False

    def printEDeviceDetails(self):
        """
        Prints details about an electronic device
        """
        print("This electronic device is " + self.typeOfDevice + ".")
        print ("IP address: " + self.IPAddress)
        print("The " + self.typeOfDevice + " is located on the " + self.location + ".")
        if self.checkAvailability() == True:
            print ("The device is currently available.")
        else:
            print ("The device is currently unavailable.")


e_device1 = EDevice ()
e_device1.setLocation("floor one")
e_device1.checkAvailability()
e_device1.printEDeviceDetails()
