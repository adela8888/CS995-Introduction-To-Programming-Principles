class EResource:
    """
    A class to represent a real-life object with its parameters. In this case
    to represent an electronic source
    """

    def __init__(self, member = None):
        """
        A constructor to initialize the instance members of the class EResource
        """
        self.author = "not set"
        self.name = "not set"
        self.ISBN = "not set"
        self.yearOfPublication = 0
        self.devices = []
        self.member = member

    def setAuthor(self, a):
        """
        Sets author of an electronic source
        """
        self.author = a

    def getAuthor(self):
        """
        Returns author of an electronic device
        """
        return self.author

    def setName(self, n):
        """
        Sets name of an electronic source
        """
        self.name = n

    def getName(self):
        """
        Returns name of an
        """
        return self.name

    def setISBN(self, i):
        """
        Sets ISBN of an electronic source
        """
        self.ISBN = i

    def getISBN(self):
        """
        Returns ISBN of an electronic device
        """
        return self.ISBN

    def setYearOfPublication (self, y):
        """
        Sets year of publication of an electronic source
        """
        self.yearOfPublication = y

    def getYearOfPublication (self):
        """
        Returns year of publication of an electronic source
        """
        return self.yearOfPublication

    def addDevice(self, d):
        """
        Adds a device to the list of devices used for reading an electronic source
        """
        self.devices.append(d)

    def getDevices(self):
        """
        Returns a list of devices used for reading an electronic source
        """
        return self.devices

    def setMember(self, member):
        """
        Sets a member who has currently borrowed a book
        """
        self.member = member

    def getMember(self):
        """
        Returns a member who has currently borrowed a book
        """
        return self.member

    def printResourceDetails(self):
        """
        Prints details about an electronic device
        """
        print("Name is the e-resource: " + self.name)
        print("Year of publication: " + str(self.yearOfPublication))
        print ("ISBN of the e-resource: " + self.ISBN)
        print("The e-resource is compatible with following devices: " + str(self.devices))

