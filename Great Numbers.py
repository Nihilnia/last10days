# Great Numbers

while True:
    userChoice = input("Give me a number or 'Q' For quit: ")
    if userChoice.lower() != "q":
        userChoice = int(userChoice)
        sumsTotal = 0
        for sums in range(1, userChoice):
            if sums % 2 != 1:
                sumsTotal += sums
    
        #questioner
        if sumsTotal == userChoice:
            print(userChoice, "a Great Number!")
        else:
            print(userChoice, "not a Great Number!")
    
    else:
        print("Quiting..")
        break