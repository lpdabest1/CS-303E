#barcode scanner
def getUserInput():
    userInput = input("Enter 12 digit barcode: ")
    return userInput

def calcOddNumDigits(strbcode):
    sum = 0
    for i in range(0, len(strbcode), 2):
        sum += int(strbcode[i])

    return sum * 3

def calcEvenNumDigits(strbcode):
    sum = 0
    for i in range(1, len(strbcode)-1, 2):
        sum += int(strbcode[i])

    return sum


def checkLastDigit(sumOdd, sumEven):
    total = sumOdd + sumEven
    strTotal = str(total)
    lastDigit = strTotal[len(strTotal)-1]
    if lastDigit == "0":
        return 0

    return 10-int(lastDigit)


'''def main():
    while True:
        bcode = getUserInput()
        calcOddNumDigits(bcode)
        #print(calcEvenNumDigits(bcode))

        strBcode = str(bcode)
        checkDigit = checkLastDigit(calcOddNumDigits(bcode), calcEvenNumDigits(bcode))
        lastDigit = strBcode[len(strBcode)-1]

        if(checkDigit == int(lastDigit)):
            print("Good")
        else:
            print("Bad")
            break
main()'''