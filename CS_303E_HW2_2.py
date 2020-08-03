def main():
    # For Part 2 of homework 2 I only fixed Question 1 and wrote what is wrong and how to correctly fix the mistakes as well as the outputs for questions: 2,3,4,6,7,8.
    # For Questions 5 and 9 I wrote my own code. Then for the last portion commented beneath my answer for Question 9, I compared the code as seen in the practice problems powerpoint in comparing If vs Else If
    
    
    #Q1: Given the code in the practice problems, the original program output would
    # not run, so I changed "+count" to +str(count) to print the value of count, but before it prints the value of count it will print "Python is fun!"
    count = 5
    if(count>0):
        print("Python is fun!")
        count = count - 1
        print("Value of count = " + str(count))
        
    #Q2: The following code below for question 2 is the exact same program as in the practie problems. The code will print
    # "Have a great day!" due to the value of the variable value is 3, therefore the if portion of the loop will not run and will run the else portion.
    value = 3
    if(value!=3):
        print("Have a nice day!")
    else:
        print("Have a great day!")
    
    #Q3: The following code below for question 3 is the same exact program in the practice problem
    # the program will output "Have a nice day!" and nothing more.
    value =3
    if(value ==3):
        print("Have a nice day!")
    elif(value >= 3):
        print("Yay! Wednesday!")
    else:
        print("Have a great day!")

    #Q4: The following code below for question 4 is the same exact program in the practice problem
    #the program will output "Have a nice day!" and "Yay! Wednesday!" as both are under if statements and value equals 3 in both test cases.
    
    if(value ==3):
        print("Have a nice day!")
    if(value >= 3):
        print("Yay! Wednesday!")
    else:
        print("Have a great day!")    

    #Q5: The program code below for question 5 is to ask the user to enter an integer number between 0 and 100.
    #If the number is less than 0 or greater than 100, display an error message.  If the number is in the correct range, display a congratulations message.  (For this you do not need verify user input).
    Range = eval(input("Enter an integer between 0 and 100: "))
    if Range < 0:
        print("error")
    elif Range > 100:
        print("error")
    else:
        print("congratulations")
        
        
    #Q6: This code below for question 6 is not valid in Python. There are many errors in this code.
    # One obvious error is that the code below does not have a score variable defined, so code will never run. Also, the if statements do not have a colon after their statements.
    # Another error, is that the assigned scores grades are never printed, also there isn't any quotations around the letter grades which is invalid in python.
        if(score >= 90)
            grade = A
        if score >= 80
            grade = B
    
    #Q7: The code below for question 7 will not run because the implementation of the else statement at the end of Question 7 is not correctly done.
    # However, the else statement can be corrected be inserting a colon after the else. Like "else:", once this correction is made, the code will output "You are passing.". ALso, the grade will be an "80".
    score = 83
    if(score >= 60):
        grade = 'P'
        print("You are passing")
        if(score >= 90):
            grade = 'A';
        if(score >= 80):
            grade = 'B'
    else    #to fix this put a colon after else
        grade = 'F';
        print("You are not passing");
    
    #Q8: The code below for question 8 will not run as there is an issue with the else statement at the end of the code for this question.
    # Once the code is fixed, it will output "You are passing" and the grade will be overwrited to a '80'.
    score = 95
    if(score >= 60):
        grade = 'P'
        print("You are passing")
        if(score >= 90):
            grade = 'A';
        if(score >= 80):
            grade = 'B'
    else   #to fix this put a colon after else
        grade = 'F';
        print("You are not passing");
    
    
    #Q9: The program below is for question 9. Give the score in float format, it will display the correct letter grade (i.e., A, B, C, D, and F)
    score = eval((input("Enter an integer: ")))
    score_float = float(score)
    if score_float >= 90:
            print('A')
    elif score_float >= 80:
            print('B')
    elif score_float >= 70:
            print('C')
    elif score_float >= 60:
            print('D')
    else:
            print('F')
    #In comparing If vs Else If, it is evident that in the first half of the comparison as listed in the practice problems the if statement will keep overriding the score if certain conditions are met.
    # However, in comparison to an else if statment, if the first condition is met with the initial if, then the else if's that proceed will not do anything. The only time the else if's will run is when the inital if statement when having a certain condition such as a raw score is not met, then the else if statements are proceeding it in seeing if the condition is met.
main()
