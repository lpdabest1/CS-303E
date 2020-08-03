import math

def main():
    
    #Question 1: Get an integer number from the user. Decide if the number is divisible by 7. Print if it is or isnt
        
        user_Input = eval(input(" Enter an integer number: "))
        if (user_Input % 7 == 0):
            print("user integer number " + str(user_Input) + " is divisble by 7")
            
        else:
            print("user integer number " + str(user_Input) + " is not divisible by 7")
            
            
    #Question 2: Write python code to display a series of calculations:
        x = -9
        y = 2
        print(str(8%3))
        print(str(6%3))
        print(str(9//4))
        print(str((6%19)+ (y+x)))
            
    #Question 3: Write python code to calculate the angular momentum
        #mass (m)
        m = eval(input("Enter a value for mass: "))
        #velocity (v)
        v = eval(input("Enter a value for velocity: "))
        #radius (r)
        r = eval(input("Enter a value for the radius: "))
        #Theta (i)
        i = eval(input("Enter a value for the angle: "))
        L = round(m*v*r*math.sin(i),4)
        print("The calculated angular momentum: " + str(L) + " in radians")

main()