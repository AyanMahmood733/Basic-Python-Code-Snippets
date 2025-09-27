i = 0 #defines variable
arr = [] #defines array
print("Would you like to Start? Y or N") 
inp = input("") #takes input for loop
if inp == "Y":
     while inp == "Y":
        print("Enter the value:")
        val = input("") #takes input to add to array
        arr.append(val) #adds value to array
        print("Would you like to add another value? Y or N")
        inp = input("")
        if inp == "Y": #goes back to while loop
            continue
        else: 
            print("Your list contains ",len(arr)," values") #prints number of values in the array
            print(arr) #prints induvidual values stored in the array

              if (distance <= maxdist) {
                if (pos <= pos2) {
                    pos2 = pos;
                }
                maxdist = distance;
                pos1 = pos;
               }
               delay(100);
               Serial.print("Max Distance at this angele: ");
              Serial.print(pos1);
              Serial.print(",");
             Serial.println(maxdist);
             }
             Serial.println(pos2);
         delay(1000);