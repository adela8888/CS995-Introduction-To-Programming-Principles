class Book:
    """
    A class to represent a real-life object with its parameters. In this case
    to represent a book
    """
    def __init__(self, member=None):
        """
        A constructor to initialize the instance members of the class Book
        """
        self.author = "not set"
        self.name = "not set"
        self.ISBN = "not set"
        self.damage = []
        self.member = member
        self.yearOfPrint = 0

    def setAuthor(self, a):
        """
        Sets author of a book
        """
        self.author = a

    def getAuthor(self):
        """
        Returns author of a book
        """
        return self.author

    def setName(self, n):
        """
        Sets name of a book
        """
        self.name = n

    def getName(self):
        """
        Returns name of a book
        """
        return self.name

    def setISBN(self, i):
        """
        Sets ISBN of a book
        """
        self.ISBN = i

    def getISBN(self):
        """
        Returns ISBN of a book
        """
        return self.ISBN

    def setDamage(self, d):
        """
        Sets damage of a book
        """
        self.damage.append(d)

    def getDamage(self):
        """
        Returns damage of a book
        """
        return self.damage

    def setMember(self, member):
        """
        Sets member who has currently borrowed a book
        """
        self.member = member

    def getMember(self):
        """
        Returns member who has currently borrowed a book
        """
        return self.member

    def setYearOfPrint(self, y):
        """
        Sets year of a print of a book
        """
        self.yearOfPrint = y

    def getYearOfPrint(self):
        """
        Returns year of print of a book
        """
        return self.yearOfPrint

    def getAvailability(self):
        """
        Checks if a book if available
        """
        if self.member is None:
            return True
        return False

    def printResourceDetails(self):
        """
        Prints all details about a book
        """
        print("Book's author: " + self.author)
        print ("Book's name: " + self.name)
        print("Book's ISBN: " + self.ISBN)
        print("Book's year of print: " + str(self.yearOfPrint))
        print("Book's damage: " + str(self.damage))
        if self.getAvailability() == True:
            print("The book is currently available. \n")
        else:
            print("The book is unavailable. \n")


b1 = Book ()
b1.setName("Raven")
b1.setISBN("9390")
b1.getAvailability()
b1.printResourceDetails()

