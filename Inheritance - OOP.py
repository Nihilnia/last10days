# vars() Function

#If we don't have showInfos() function yet, we can use vars() function for that

#Example:

class Students():

    def __init__(self, studentName, studentNumber):
        self.studentName = studentName
        self.studentNumber = studentNumber
    
studentNihil = Students("Nihil", 1)

print(vars(studentNihil))




#### INHERITANCE ####

#first, let's create a class

class Spotify():

    def __init__(self, trackName, trackID, artist):
        self.trackName = trackName
        self.trackID = trackID
        self.artist = artist

    def showInfos(self):
        print("""***That object created with Spotify***)
        Artist: {}
        Track Name: {}
        Track ID: {}""".format(self.artist, self.trackName, self.trackID))

#Now let's create another class

class Fizzy(Spotify):
    
    def showInfos(self):
        print("""***That object created with Fizz***)
        Artist: {}
        Track Name: {}
        Track ID: {}""".format(self.artist, self.trackName, self.trackID))


#Now we can create an object with using Fizzy class.
# Because that class have Spotify's functions with Interitance.

track0001 = Spotify(artist = "nihil", trackName = "nothing", trackID = 0)
track0002 = Fizzy(artist = "Gloria", trackName = "Project", trackID = 1)

print("Spotify one:")
track0001.showInfos()

print("Fizzy one:")
track0002.showInfos()


# Make another example:

class Developers():

    def __init__(self, devName, devLangs, devRaise):
        self.devName = devName
        self.devLangs = devLangs
        self.devRaise = devRaise
    
    def showInfos(self):
        print("""
        - ALL INFORMATIONS ABOUT DEVELOPER '{}' -
        Languages: {}
        Raise: {}     
        """.format(self.devName, self.devLangs, self.devRaise))

    def raiseUpgrade(self, upgradeAmount):
        oldRaise = self.devRaise
        self.devRaise += upgradeAmount
        print("""
        - RAISE UPGRADE SUCCESFUL -
        Old Raise was: {}
        New Raise: {}
        """.format(oldRaise, self.devRaise))

dev0001 = Developers("nihil", "Python", 2000)
dev0001.showInfos()
print("Raise upgrade..")
dev0001.raiseUpgrade(upgradeAmount = 500)
dev0001.showInfos()