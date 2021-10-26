
# Program final- truck rental 
#-------------------------------------------------------------------
# Variable                Type       Purpose
#-------------------------------------------------------------------
#fltChoice               float       store user input
#fltDaily                float       sotre daily charge
#fltMile                 float       store mileage charge
#fltWeekly               float       store weekly charge
#fltWeeklyMC             float       store weekly mileage after 200
#strCLassification       string      store user input
#fltNumD                 float       store num of days
#fltnumM                 flaot       store num of miles
#fltnumW                 float       store num of weeks
def main():
    fltChoice = 'a'
    fltDaily = [19.95, 29.95, 39.95]
    fltMile = [0.59, 0.79, 0.85]
    fltWeekly = [125.68, 188.68, 251.68] #Weekly Rental
    fltWeeklyMC = [0.59, 0.79, 0.85] #Weekly rental after 200
    strRental = 'p'
# Creat variables and assign values
   
    while fltChoice != 'x':
        menu1()
        print("")
        fltChoice = input("Make a selction: ")
        print("")

        if fltChoice == "a" or fltChoice == 'A':
            Class()
            strClassification = input("Which Class of truck do you want to rent? ")
            
            if strClassification == 'A' or strClassification == 'a':
                Classification(fltDaily[0], fltMile[0], fltWeekly[0], fltWeeklyMC[0])
                   


                
            elif strClassification == 'B' or strClassification =='b':
                Classification(fltDaily[1], fltMile[1], fltWeekly[1], fltWeeklyMC[1])

            elif strClassification == 'C' or strClassification =='c':
                Classification(fltDaily[2], fltMile[2], fltWeekly[2], fltWeeklyMC[2])
            else:
                print("Class not recognized, please try again.")
        elif fltChoice == "x" or fltChoice == "X":
            print("Goodbye!")
        else:
            print("Input not recognized, please try again.")
                
def menu1():
    print("================================================")
    print("Truck Rental Calculator")
    print("================================================")
    print ("a: Rent Truck")
    print ("x: Exit")
    

def ClassAD(f1, f2, f3, f4):
    fltDailyC = (f1 * f2)
    fltDailyM = (f3 * f4)
    fltTotal = (fltDailyC + fltDailyM)
    print("--------------------------")

    print ("The cost is  $", '{0:.2f}'.format(fltTotal))
    
    print("--------------------------")

def ClassAW(f1, f2, f3, f4):
    fltWeeklyBase = (f1 * f2)
    if f3 > 200:
        f3 = f3 - 200
        fltWeeklyMile = (f3 * f4)
        
        fltTotal = (fltWeeklyBase + fltWeeklyMile)
        print("--------------------------")

        print ("The cost is  $", '{0:.2f}'.format(fltTotal))

        print("--------------------------")

    else:
        fltTotal = fltWeeklyBase
        print("--------------------------")

        print ("The cost is  $", '{0:.2f}'.format(fltTotal))

        print("--------------------------")

    
def Class():
    print("--------------------------")
    print("")
    print("A")
    print("")
    print("B")
    print("")
    print("C")
    print("")
    print("--------------------------")

def Classification(c1, c2 ,c3, c4):
    print("")
    strRental = input("(W)eekly or (D)aily rental?: ")           
    if strRental == "D" or strRental == "d":
        print("")
        fltNumD = float(input("How many days do you need the Truck? "))
        print("")
        fltNumM = float(input("How many Miles will be driven? "))
        print("")
        ClassAD(fltNumD, c1, fltNumM, c2)
    elif strRental == "W" or strRental == "w":
        print("")
        fltNumW = float(input("How many weeks do you need the Truck? "))
        print("")
        fltNumM = float(input ("How many Miles will be driven? "))
        print("")
        ClassAW(fltNumW, c3, fltNumM, c4) 
    else:
        print("Input not recognized, please try again.")

# Display outut to user


main()
# Add Output of finale program as Comments 
##================================================
##Truck Rental Calculator
##================================================
##a: Rent Truck
##x: Exit
##
##Make a selction: a
##
##--------------------------
##
##A
##
##B
##
##C
##
##--------------------------
##Which Class of truck do you want to rent? b
##
##(W)eekly or (D)aily rental?: 2
##Input not recognized, please try again.
##================================================
##Truck Rental Calculator
##================================================
##a: Rent Truck
##x: Exit
##
##Make a selction: a
##
##--------------------------
##
##A
##
##B
##
##C
##
##--------------------------
##Which Class of truck do you want to rent? b
##
##(W)eekly or (D)aily rental?: d
##
##How many days do you need the Truck? 2
##
##How many Miles will be driven? 130
##
##--------------------------
##The cost is  $ 162.60
##--------------------------
##================================================
##Truck Rental Calculator
##================================================
##a: Rent Truck
##x: Exit
##
##Make a selction: a
##
##--------------------------
##
##A
##
##B
##
##C
##
##--------------------------
##Which Class of truck do you want to rent? c
##
##(W)eekly or (D)aily rental?: w
##
##How many weeks do you need the Truck? 1
##
##How many Miles will be driven? 210
##
##--------------------------
##The cost is  $ 260.18
##--------------------------
##================================================
##Truck Rental Calculator
##================================================
##a: Rent Truck
##x: Exit
##
##Make a selction: x
##
##Goodbye!
