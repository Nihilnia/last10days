#Super() function.
# If we got a function from another class we don't have to define same variables at current function.
# - Look at the line 49!

#let's create a Class

class Skype():

    def __init__(self, userId, userNick, userTotalCredits):
        print("Skype class worked!")
        self.userId = userId
        self.userNick = userNick
        self.userTotalCredits = userTotalCredits

    def showInfos(self):
        print("""
        INFORMATIONS ABOUT USER
        User ID:    {}
        User Nick:  {}
        User Credit:    {}
        """.format(self.userId, self.userNick, self.userTotalCredits))
    
    def changeInfos(self, newId, newNick):
        oldUserId = self.userId
        oldUserNick = self.userNick
        self.userId = newId
        self.userNick = newNick
        print("""
        INFORMATIONS CHANGED!
        New User ID:    {}  Old User ID:    {}
        New User Nick:  {}  Old User Nick:  {}
        """.format(self.userId, oldUserId, self.userNick, oldUserNick))

    def changeUserCredits(self, newCredit):
        oldCredit = self.userTotalCredits
        self.userTotalCredits = newCredit
        print("""
        USER CREDIT CHANGED!
        Remaining Credit:   {}
        Old Credit: {}
        """.format(self.userTotalCredits, oldCredit))

#Now let's create another class and get properties from first one (with Inheritance!)

class Discord(Skype):
    
    def __init__(self, userId, userNick, userTotalCredits, callNumber):
        #Now let's use super function
        super().__init__(userId, userNick, userTotalCredits)
        self.callNumber = callNumber

    def showInfos(self):
        print("""
        INFORMATIONS ABOUT USER
        User ID:    {}
        User Nick:  {}
        User Credit:    {}
        User Call Number:   {}
        """.format(self.userId, self.userNick, self.userTotalCredits, self.callNumber))

discordUser = Discord(userId = "2890", userNick = "nihil", userTotalCredits = 5000, callNumber = 88)
discordUser.showInfos()

skypeUser = Skype(userId = 3, userNick = "Gloria", userTotalCredits = 900)
skypeUser.showInfos()

# Let's try other functions

discordUser.changeUserCredits(1000)
discordUser.showInfos()