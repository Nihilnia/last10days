# Armstrong Numbers

from time import sleep

while True:
    userChoice = input("Give me a number or 'Q' For quit: ")
    if userChoice.lower() != "q":
        sumsTotal = 0
        numberLenght = len(userChoice)
        for x in userChoice:
            sumsTotal += pow(int(x), numberLenght)
    
        #questioner
        if sumsTotal == int(userChoice):
            print(userChoice, "a Armstrong Number!")
        else:
            print(userChoice, "not a Armstrong Number!")
    
    else:
        print("Quiting..")
        sleep(2)
        break