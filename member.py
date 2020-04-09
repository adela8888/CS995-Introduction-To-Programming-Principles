class Member:
    """
    A class to represent a real-life object with its parameters. In this case
    to represent a person who has a membership in the library
    """

    def __init__(self):
        """
        A constructor to initialize the instance members of the class Member
        """
        self.firstName = "not set"
        self.secondName = "not set"
        self.studentNumber = "not set"
        self.listOfBooksBorrowed = []
        self.messages = []

    def setFirstName(self, n):
        """
        Sets first name of a member
        """
        self.firstName = n

    def getFirstName(self):
        """
        Returns first name of a member
        """
        return self.firstName

    def setSecondName(self, s):
        """
        Sets second name of a member
        """
        self.secondName = s

    def getSecondName(self):
        """
        Returns second name of a member
        """
        return self.secondName

    def setStudentNumber(self, m):
        """
        Sets student number of a member
        """
        self.studentNumber = m

    def getStudentNumber(self):
        """
        Returns student number of a member
        """
        return self.studentNumber

    def addBookBorrowed(self, b):
        """
        Adds a borrowed book to the list of currently borrowed books by a member
        """
        self.listOfBooksBorrowed.append(b)

    def getListOfBooksBorrowed(self):
        """
        Returns a list of currently borrowed books by a member
        """
        return self.listOfBooksBorrowed

    def addMessage (self, me):
        """
        Adds message for a member
        """
        self.messages.append(me)

    def getAllMessages (self):
        """
        Returns all messages of a member
        """
        return self.messages

    def printAllMessafes (self):
        """
        Prints all messages of a member
        """
        for i in self.messages:
            print (i)

    def getNumberOfBooksBorrowed(self):
        """
        Returns a number of books currently borrowed by a member
        """
        return len(self.listOfBooksBorrowed)

    def printNumberOfBooksBorrowed(self):
        """
        Prints a number of books currently borrowed by a member
        """
        print(("The number of books currently borrowed: " + str(len(self.listOfBooksBorrowed))))

    def printMemberDetails(self):
        """
        Prints details of a member
        """
        print("Name: " + self.firstName + " " + self.secondName)
        print("Student's number: " + self.studentNumber)
        print("List of books currently borrowed: " + self.listOfBooksBorrowed)

    def printBorrowedBooksDetails(self):
        """
        Prints details of all books currently borrowed by a member
        """
        for i in self.listOfBooksBorrowed:
            i.printResourceDetails()