import math


def main():
    y = 5
    z = 2
    #Really Short Problems
    #Question 1
    x = y + z
    print("The sum of y and z is: " + str(x))
    #Question 2
    uName = "The University of Texas"
    print(uName)
    #Question 3
    print(int(11.56 * 100))
    #Question 4
    print(round(4.6))
    #Question 5
    print(int(42.6))
    #Question 6
    print(21 % 4)
    #Question 7
    print(10 // 3)

    #The Longer Problems
    #Question 8
    userInput = int((input("Enter a number to determine if even or odd: ")))
    numDetermine = (userInput % 2)
    if numDetermine > 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")

    #Question 9
    userOrder = eval((input("How many dozens cookies do you want to order:  ")))
    totalCookies = userOrder * 12
    print("Total number of cookies ordered by the users is: " + str(totalCookies))

    #Question 10
    userLength = eval((input("Enter a length:  ")))
    userWidth = eval((input("Enter a width:  ")))  # print (width*length)
    area = userLength * userWidth
    print("Area determined by the length and width entered by the user is: " + str(area))

    #Question 11
    userDiameter = eval((input("Enter a diameter for the circle:  ")))
    circumference = 2 * math.pi * userDiameter / 2
    areaCircle = math.pi * (pow(userDiameter/2, 2))
    print("The circumference of the circle is: " + str(circumference))
    print("The area of the circle is: " + str(areaCircle))

    #Question 12
    #circular cone volume = (1/3)pi*r^2*h
    userRadius = eval((input("Enter a radius:  ")))
    userHeight = eval((input("Enter a height:  ")))
    volume = (1 / 3) * math.pi * (pow(userRadius, 2)) * userHeight
    print("The volume of water that the circular cone can hold is: " + str(volume))

    #Question 13
    #calculated mean
    userNumber1, userNumber2, userNumber3 = eval((input("Enter three numbers:  ")))
    mean = (userNumber1 + userNumber2 + userNumber3) / 3
    print("The average (mean) of the numbers entered is: " + str(mean))


main()


