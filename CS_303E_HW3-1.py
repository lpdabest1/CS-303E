import random

def main():
    #Question 1
    #Write a For loop that displays to the screen the multiples
    # of 3 starting with 9 and continuing until 27. Rewrite using a While Loop.
    for x in range(9, 28, 3):
        print(x)

    y = 9
    while y < 28:
        print(y)
        y += 3

#Question 2
#Write code to fill a List with the values from 5 to -5 using a For Loop. Rewrite using a While Loop.
    myList = []
    for x in range(5, -6, -1):
        myList.append(x)
    print(myList)

    #myList2 = []
    #y = 5
    #while(y >= -5):
    #    myList2.append(y)
    #    y -= 1
    #print(myList2)

#Question 3
#Write code to fill a List with only even numbers from -10 to 10
    #(i.e., -10, -8, …, 8, 10).
    aList = []
    for x in range(-10, 11, 2):
        aList.append(x)
    print(aList)

#Question 4
#Write code to display the numbers 1-5 with the @ symbol between each number.
    print(1,2,3,4,5, sep='@')

#Question 4
    #for x in range(1, 6):
    #    if(x == 5):
    #        print(str(x))
    #    else:
    #        print(str(x) + "@", end ="")
#Question 5
#I love coding and python
    print('I love {0} and {1}'.format('coding', 'python'))
    print("I love {1} and {0}".format('coding', 'python'))

    print('Hello {name}, {greeting}'.format(greeting = "How are you?",
                                            name = input("What is your name?")))

#Question 6
#[9, 1, 8, 99, 45, 78, 14, 2, 7, 69]. Print until 14
    aList = [9, 1, 8, 99, 45, 78, 14, 2, 7, 69]
    for x in range(0, len(aList)):
        if aList[x] != 14:
            print(aList[x])
        else:
            break

    #for x in aList:
    #    if x != 14:
    #        print(x)
    #    else:
    #        break

    #x = 0
    #while(x < len(aList)):
    #    if aList[x] != 14:
    #        print(aList[x])
    #    else:
    #        break
    #    x += 1
        
#Question 7
    sum = 0
    for x in aList:
        sum+= x
    
    print(sum)
        
        
    #Question 8
    for x in range(1, 5):
        for y in range(0, x):
            print('*', end="")
        print()

    #Question 9
    for x in range(5,0,-1):
        for j in range(0,x):
            print('*', end="")
        print()
        


    #Question 10
    aList = []
    for x in range(0,10): # or range(0,10)
        aList.append(round(random.random(), 4))
    print(aList)
        
        
    sum = 0
    for x in aList:
        sum+= x    
    print(sum)    
    
    mean= round((sum)/(len(aList)),4)
    print(mean)
    print(aList.index(max(aList)))
    print(aList.index(min(aList)))
    
    # Notes from last class
    # print(random.random())
    # print(round(random.random(), 4))
    # print(random.randint(0, 5)) # Range of integers
    
    # To print 10 random integer
    
    #'''aList = []
    #for x in range(10): # or range(0,10)
        #aList.append(round(random.random(), 4))
    #print(aList)'''

main()
