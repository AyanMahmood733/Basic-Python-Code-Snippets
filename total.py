x = 0 #defines variable
z = 0 #defines variable
print("Would you like to enter a number? Y or N")
more = input("") #takes variable for loop
while more == "Y":
    print("Enter your number ")
    z = input()
    x = int(x) + int(z) #calculation
    print("Do you wish to add another number? Y or N")
    more = input("") #takes input for if command
    if more == "N": #prints values if the user is done
        print(x)
        print("Do you wish to start again?")
        more = input("")
        if more == "Y": #redefines value and restarts
            x = 0
            continue
        if more =="N": #exits
            exit
