def main():
    numbersList = []
    while (True):    
        try:
            #User must enter a number that is of an int type
            userInput = (input("Enter a number (int): "))
            #User input string "STOP" to end and exit the program but any other string will just be skipped
            if(userInput == "STOP"):
                break
            userInput = int(userInput)
            numbersList.append((userInput))
        except ZeroDivisionError:        
            print("You cannot divide by zero..")
        except ValueError:
            print("That was not a number (int)...")
        except:
            print("Something went wrong")
    
    meannumbersList = sum(numbersList)/len(numbersList)
    minnumbersList = min(numbersList)
    maxnumbersList = max(numbersList)
    numbersList.sort()
    print("Sorted List: " + str(numbersList))
    print("Mean: "+ str(meannumbersList))
    print("Min: " + str(minnumbersList))
    print("Max: " + str(maxnumbersList))
    
main()