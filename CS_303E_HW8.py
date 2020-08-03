#Sorting Algorithms Notes
# See where the other elements go in thr declared sorted list and keep adding until all elements are sorted in the sorted list.
# Bubbke is really handy for when the list is mostly already sorted
# If I havent really done a sort list, I should use an Insertion Sort Method
# For input use split on HW #8

def main():
    #user_Input is the user input of integers being added to a list
    # Looked up how to do map() function in python from the website given below in order to shortcut how to put user input to a list while converting to inetegers without quotation marks
    # map is map(function, iterable), however we do this in a list form
    # The website is: https://www.geeksforgeeks.org/python-map-function/
    user_Input = list(map(int,input("Enter numbers to be sorted: " + "").split(" ")))

    selectionList = selectionSort(user_Input)
    print("Selection sort =", selectionList)
    insertionList = insertionSort(user_Input)
    print("Insertion sort =", insertionList)
    bubbleList = bubbleSort(user_Input) 
    print("Bubble sort =", bubbleList)

    
def selectionSort(selectionList):
    for i in range(0, len(selectionList), 1):
        maxValue = i
        for j in range(i+1, len(selectionList)):
            if selectionList[j] > selectionList[maxValue]:
                maxValue = j
        tempVariable = selectionList[i]
        selectionList[i] = selectionList[maxValue]
        selectionList[maxValue] = tempVariable
    return selectionList

def insertionSort(insertionList):
    for i in range(1, len(insertionList)):
        #Elements to be compared with the first "sorted" one
        currentValue = insertionList[i]
        index = i
        # To determine how to do the swapping of the current sorted value and the compared value, I used a website
        # The website is: http://interactivepython.org/courselib/static/pythonds/SortSearch/TheInsertionSort.html
        #comparing the unsorted elements of the list to the sorted portion of the list and swapping
        if index > 0 and insertionList[index-1] < currentValue:
            insertionList[index] = insertionList[index-1]
            index = index - 1
        insertionList[index] = currentValue
    return insertionList
        
def bubbleSort(bubbleList):
    for i in range(0, len(bubbleList),1):
        for j in range(i, len(bubbleList)):
            if bubbleList[j] > bubbleList[i]:
                tempVariable = bubbleList[i]
                bubbleList[i] = bubbleList[j]
                bubbleList[j] =tempVariable
    
    return bubbleList
    
    
main()