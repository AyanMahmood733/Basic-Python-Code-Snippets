x = 0 #where x is the counter
y = 0 #where y is the sum
z = 0 #where z is the mean
print("Do you wish to add a number? Y or N")
more = input("") #takes value for loop
while more == "Y": #starts loop
    x = x + 1
    print("Enter your number:")
    num = input("")
    y = int(y) + int(num) #calculation
    print("Do you wish to add another number?")
    more = input("")
    if more == "N": #prints values
        z = y / x
        print(z)
        print("Do you wish to start again?")
        more = input("")
        if more == "Y": #resets values to start from the top or exit
            x = 0
            y = 0
            z = 0
            continue
        elif more == "N":
            exit
