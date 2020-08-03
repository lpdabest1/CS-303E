def main():

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    aList = [6, 8, 10, 12]

    bList = [1, 3, 5, 7]

    #Question 1

    #Write the python code to concatenate two Lists: aList first, followed by bList.
    # Rewrite the python code to concatenate them in the opposite way (bList before aList).
    print(aList + bList)
    cList = aList + bList
    print(cList)
    print(bList + aList)

    #Question 2
    #Write the Python code to insert the number 6 in the middle of aList.
    #aList.insert(2,6)
    aList.insert(len(aList)//2, 6)
    print(aList)


    #Question 3: Write a python program that counts the number of times 6 appears in aList and displays the result to the screen for the user.


    print('How many times 6 appears in aList: ' + str(aList.count(6)))

    #Question 4: Write the Python code to remove or clear all the items in bList

    new_bList = bList

    new_bList.clear()

    print('To Check if all items are cleared from bList: '+str(new_bList))

    #Question 5: Write the python code to calculate the average of the values in the aList.

    mean = sum(aList)/float(len(aList))
    print('The average of the values in aList is: '+str(mean))

    #Question 6: print week, day, month, year

    week = eval(input("Enter weekday:")) - 1
    month = eval(input("Enter month:")) - 1
    day = input("Enter day: ")
    year = input("Enter year:")
    print(days[week] + ": " + months[month] + " " + day + ", " + year)

    #Question 7: my list adjustments

    myList = [42, 3, 19, 5]

    myList.pop(2)
    myList.insert(2, 45)
    print(myList)

    myList.pop(3)
    myList.insert(3, 55)
    print(myList)

    myList.append(99)
    print(myList)

    myList.insert(0, 1)
    print(myList)

    print('Final myList: '+str(myList))


main()


