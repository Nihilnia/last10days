#Object Oriented Programming

# First of all let's create a class

class ExampleOne():
    nick = "nihil"
    age = 24

#Now let's reach our variables from class

print(ExampleOne.nick)
print(ExampleOne.age)

# We can create variables with using objects

user = ExampleOne()
print("This is information of user:", user)

#or, spesific one:
userNick = ExampleOne.nick
print("This is Nick of the user:", userNick)

#But that ways we can't make any change on objects, variables.

#Now let's create another class

class Students():

    def __init__(self, studentName, studentNumber):
        self.studentName = studentName
        self.studentNumber = studentNumber #actually we can give any name

student0001 = Students("Nihil", 1) #Here is I didn't insert object names, I just insert as order.
#Note: If we don't insert object names specificly then given by order.

student0002 = Students(studentNumber = 2, studentName = "Gloria")

print("Student's List:\n\n")
print("""Names: {}
Numbers: {}""".format((student0001.studentName, student0002.studentName),
(student0001.studentNumber, student0002.studentNumber)))

#LMAO THIS BETTER.



#### METHODS ON CLASSES ####
class Developers():

    def __init__(self, name, language):
        self.name = name
        self.language = language

    # Now I will create another function for some change
    def ShowDevInfos(self):
        print("Dev name: {}, Dev language: {}".format(self.name, self.language))

    def ChangeDevLang(self, newLang):
        self.language = newLang
        print("""Language change succesful!
        Developer {}'s new Language {}""".format(self.name, self.language))

    def AddNewLanguage(self, addNewLangDev):
        self.language = ", " + addNewLangDev
        print("""Language succesfuly added!
        Developer {}'s all Languages {}""".format(self.name, self.language))

dev0001 = Developers("Nihil", "Python")
dev0001.ShowDevInfos()
# userInput = input(("Do you wanna change the language of Dev0001?: Y/N"))
# if userInput.upper() == "Y":
#     newLanguageFromUser = input("New language: ")
#     dev0001.ChangeDevLang(newLang = newLanguageFromUser)
# else:
#     pass

userInput = input(("Do you wanna add the language of Dev0001?: Y/N "))
if userInput.upper() == "Y":
    newLanguageFromUser = input("New language: ")
    dev0001.AddNewLanguage(addNewLangDev = newLanguageFromUser)
else:
    pass

