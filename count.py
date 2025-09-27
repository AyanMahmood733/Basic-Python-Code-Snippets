x = 0 #defines variable
more = input("Would you like to enter a number? Y or N: ") #takes input for loop
while more == "Y":
    num = input("Enter your number: ")
    x = x + 1 #calculation
    more = input("Would you like to enter another number? Y or N: ")
    if more == "N": #prints value
        print(x)
        print("Would you like to exit? Y or N")
        more = input("") #asks whether program should exit or restart
        if more == "N": #exits
            exit
        if more == "Y": #redefines variable, starts from top
            x = 0
            continue

