#   Homework 10:
''' Question 1:
    Overall, this program is supposed to covert certain integer values to a time (clock) format.
    However, the code first goes about this by creating a class with three defined parameters which are:
    hours, minutes, seconds. Furthermore, the class uses the "hard-coded" values to format the code to military time
    under the class function func1 and func1b. Afterwards, the time goes under function fun2_a to converted to
    regular standard time.
'''


''' Question 2:
    In overall, class c2 in this code represents a method that will have certain functions to carry out the time 
    conversion. The class as I mentioned in Question 1 has three parameters that the programmer defined as t1, t2, t3.
    The class allows for the code to be much more organized with function within the class that can be called to carry out both conversions of the time format 
    that are based on the values of t1,t2,t3. The class furthermore, also has a printout statement that correctly prints the parameters that were defined.  
'''

''' Question 3:
    In the original code, function10 (in my code is the main) functions as a main that carries out the calculations and "running of the code".
    Function10 has the defined values for the three time parameters. Also, the instance of the class c2 is defined (Variable x1 created) in function10, which we could now use to run the function in the class
    for the particular instance/variable. The functions that are defined within the class are later called and used on the instance (x1).

'''

''' Question 4:*
    In the original code, function3 functions to take a user input (which is assumed to be an integer); however, if the user inputs an invalid input like a string, then the function returns all of
    valid user inputs into the aList and returns it because an invalid input goes to the exceptions(NameError, TypeError,etc).
'''

''' Question 5:
    The list aList is being used to store the values of t1, t2, and t3.
'''

''' Question 6:
    Nums is being used to store the values at the index of aList from function3_ (which of course has the parameter list aList)
'''

''' Question 7:
    The format of the input into the program is an integer which is evaluated by the eval function to see if the input is valid. The format of the input(s) represent that the only data type that will be accepted are int(s)
    , which means that the exceptions will catch any strings, floats, or any other error such as type error, name error, etc.
'''

''' Question 8:
    The kind(s) of input that causes the program to stop are any input that is not an integer (int) type such as: strings, floats, etc.
'''

''' Question 9:
    The methods that are not needed and do not serve a purpose to the over-all program are: function3_ , and function3. 
'''

''' Question 10:
    There are various things wrong with function3. First off, for this code, no user input os needed  and function 3 fails to return the values inputted by the user into the list aList.
    Furthermore, the function in general for the purpose of this assignment is not even needed/does not serve a purpose.
    Also, functions basically tries to catch when the user is entering an invalid input which is caught by the exceptions; otherwise, the code continues to run as normal
    allowing the user to continue entering valid inputs (integers).
'''


''' Question 11:
    The purpose of the method setC1 is to determine the specific assignment of the parameters t1, t2, and t3 based in certain conditions as defined in the method.
    thus the conditions of the parameters help distinguish the three into values for hour(s), minute(s), and second(s). Furthermore, setC1 checks to see if the values are a valid time
    based on the categories of hour(s), minute(s) and second(s) which are on this scale respectively: (0-23), (0-59), (0-59), if not then they equal a value of either 0 or themselves.
    
'''

''' Question 12:
    The purpose of the method func1 in the class c2 is to print the values for the parameters t1, t2, and t3.
    The purpose of the method func2 in the class c2 is to do the conversion of the parameter t1 into hours.
    The purpose of the method func2_a in the class c2 is to do the conversion of the parameter t2 into minutes.
    The purpose of the method func2_b in the class c2 is to do the conversion of the parameter t3 into seconds.
    The purpose of the method func1b in the class c2 is to the standard time conversion of am and pm based on the value of the 
    parameter t1 either being between 0-12 (am) or 12-24 (pm), etc.
'''

''' Question 13:
    The identifiers used in this program are so problematic due to a variety of reasons. The identifiers are named inaccurately and very poorly. 
    In addition, there are many instances where the identifiers for various functions or variables are either never called or are called incorrectly.
    Also, for the new revised code I changed many of the identifiers to be much more meaningful/recognizable.
'''

aList = []
class c2:
    def __init__(self, t1=0, t2=0, t3=0):
        self.setC1(t1, t2, t3)
    def setC1(self, t1 = 99, t2 = 99, t3 = 99):
        if t1 >= 0 and t1 < 24:
            self.t1 = t1
        else:
            self.t1 = 0
        if t2 >= 0 and t2 < 60:
            self.t2 = t2
        else:
            self.t2 = 0
        if t3 >=0 and t3 < 60:
            self.t3 = t3
        else:
            self.t3 = t3

    def printTime(self):
        print("{0}:{1}:{2}".format(self.t1, self.t2, self.t3))

    def func2(self, x = 1):
        y = 10
        self.t1 += y + x
        self.t1 -= y
        self.t1 = self.t1 % 24
    def standardTime(self, x = 1):
        self.t2 += x
        if(self.t2 > 60):
            self.t2 = self.t2 % 60
            self.t1 += 1
    def func2_b(self, x = 1):
        self.t3 += x
        if(self.t3 > 60):
            self.t3 = self.t3 % 60
            self.func2(1)

    def militrayTime(self):
        t1_final = 0
        ending = "m"
        if self.t1 == 0 or self.t1 == 12:
            t1_final = 12
        else:
            t1_final = self.t1 % 12
        if self.t1 < 12:
            print("{0}:{1}:{2} {3}".format(t1_final, self.t2, self.t3, "a"+ending))
        else:
            print("{0}:{1}:{2} {3}".format(t1_final, self.t2, self.t3, "p"+ending))

def main():
    t1 = 2
    t2 = 58
    t3 = 14
    time = c2(t3, t2, t1)
    time.printTime()
    time.militrayTime()
    for x in range(0, 6, 1):
        if x % 2 > 9:
            x = 99
    time.standardTime(x)
    time.printTime()
    time.militrayTime()

    time.printTime()


main()

