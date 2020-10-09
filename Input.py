import time


def main():
    ##Call name 
 name()
 ## tell program to wait 3 seconds
 time.sleep(3)
 #call age
 age()

def age():
    # Ask for age 
    myAge = input("How Old are you? ")
    #Add 10 to age input
    print ("You will be", str(int(myAge) + 10), "In ten years!")
    print("------------------------------------------------------")


def name():
    print("------------------------------------------------------")

    # Ask for name
    myName = input("Hello! What is your name? ")
    # get length og name
    LengthName = len(myName)
    #print out how long the name is
    print ("Your name is", LengthName, "Letters long!")
    print("------------------------------------------------------")


##call main
main()