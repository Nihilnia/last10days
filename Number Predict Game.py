# Number Predict Game

import random, time

while True:
    print("""##### NEW GAME STARTING! ####\n\n
    I have a number in my mind between 1-10. 
    Let's predict which number is that!
    \"Press Q for quit.\"\n\n""")

    print("You have 3 predict right.")

    ourNumber = random.randint(1, 11)
    userRight = 3
    
    while True:
        if userRight != 0:
            userInput = input("Which number?: ")
            userInput = int(userInput)
            if userInput != ourNumber:
                userRight -= 1
                print("Wrong predict babe. Your remaining predict right:", userRight)
            else:
                print("Well done! My number was:", ourNumber)
                break
        else:
            print("No predict remaining. My number was:", ourNumber, "\n\n")
            break