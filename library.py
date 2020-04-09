class Library:
    """
    A class to represent a real-life object with its parameters. In this case
    to represent a library
    """
    def __init__(self):
        """
        A constructor to initialize the instance members of the class Library
        """
        self.name = "not set"
        self.location = "not set"
        self.listOfResources = []
        self.listOfEDevices = []
        self.listOfMember = []

    def setName (self, na):
        """
        Sets name of a library
        """
        self.name = na

    def getName (self):
        """
        Returns name of a library
        """
        return self.name

    def setLocation (self, lo):
        """
        Sets location of a library
        """
        self.location = lo

    def getLocation (self):
        """
        Returns location of a library
        """
        return self.location

    def addResource(self, a):
        """
        Adds a resource to the list of resources in the library
        """
        self.listOfResources.append(a)

    def getListOfResources(self):
        """
        Returns list of resources in the library
        """
        return self.listOfResources

    def addMember (self, me):
        """
        Adds a member to the list of library members
        """
        self.listOfMember.append(me)

    def getListofMembers (self):
        """
        Returns list of library members
        """
        return self.listOfMember

    def checkResourseExists(self, i):
        """
        Checks if a resource exits
        """
        return i in self.listOfResources

    def editResourceTitle (self, resource, newName):
        """
        Edits title of a resource. Raises exception if it does not exit
        """
        if self.checkResourseExists (resource):
            resource.setName (newName)
        else:
            raise Exception ("This resource is not in the library catalogue.")

    def getResource(self, resource):
        """
        Returns a resource if it is in a list of resources. Otherwise returns None
        """
        if resource in self.listOfResources:
            return resource
        return None

    def printResourceByISBN (self, ISBN):
        """
        Prints details of all resources with a given ISBN
        """
        for resource in self.listOfResources:
            if (resource.getISBN() == ISBN):
                resource.printResourceDetails ()

    def printResourceByAuthor(self, author):
        """
        Prints details of all resource by a given author
        """
        for resource in self.listOfResources:
            if (resource.getAuthor() == author):
                resource.printResourceDetails()

    def removeResource(self, resource):
        """
        Removes a resource from a list of resources
        """
        if resource in self.listOfResources:
            self.listOfResources.remove(resource)
        else:
            raise Exception("There is no such resource.")

    def removeResourceByPosition(self, m):
        """
        Removes a resource from a list of resources by calling its position in the list
        """
        del self.listOfResources [m]

    def numberOfResources (self):
        """
        Counts a number of all resources in the library
        """
        return len (self.listOfResources)

    def addResource (self, r):
        """
        Adds a resource to the list of resource in the library if it is not
        already there. Otherwise raises exception
        """
        if r not in self.listOfResources:
            self.listOfResources.append(r)
        else:
            raise Exception ("The resource is already in the library catalogue.")

    def lendResource (self, resource, member):
        """
        Assigns a member to a resource if the resource's member is None and the resource
        is in the list of resources and a member has less than 5 books borrowed currently
        """
        if resource in self.listOfResources and resource.getMember() is None and member.getNumberOfBooksBorrowed() < 5:
            member.addBookBorrowed (resource)
            resource.setMember (member)

    def returnResource (self, resource, member, damage = False, damageRecord= None):
        """
        Removes a resource from a list of books borrowed and adds records
        if a resource was damaged
        """
        if resource in member.listOfBooksBorrowed:
            member.listOfBooksBorrowed.remove (resource)
            resource.setMember (None)
            if damage:
                resource.damage.append(damageRecord)

    def sendMessage (self,message):
        """
        Sends a message to all members who has at least one resource currently borrowed
        """
        for resource in self.listOfResources:
            if resource.getMember() is not None:
               resource.getMember().addMessage(message)

    def printEveryResourcelDetails (self):
        """
        Prints details of all resources in the library
        """
        for i in self.listOfResources:
            if type(i) == Book:
                print ("This is a book")
            else:
                print ("This is an e-resource")
            i.printResourceDetails()




