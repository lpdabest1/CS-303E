class Pizza:
    count = 0
    order = []

    def __init__(self, size , curst, sauce, toppings,done):
        self.orderdetails = []
        self.size = size
        self.curst = curst
        self.sauce = sauce
        self.toppings = toppings
        self.done = done


def sauceMenu():
    while True:
        try:
            sauce = input('How much sauce do you want? (N)one, (E)xtra, or (L)ight ')
            if sauce in ['N','n','E','e','L','l']:
                return sauce
            else:
                print("That is not a level of sauce we have. Try again")
        except:
            break

def toppingMenu():
    print('(E)xtra cheese, (M)ushrooms, (G)oat cheese\n(T)omatoes, (P)ineapple, (F)resh veggies\n(K)alamata olives, (G)reen olives, (B)lack olives\nB(A)con, Pepperon(I), (H)am, Bee(F)')
    while True:
            toppings = input('Enter a topping or done: ')
            if toppings in ['E','e','M','m','G','g','T','t','P','p','F','f','K','k','B','b','A','a','I','i','H','h','F','f']:
                pass
            elif toppings in ['DONE','done','DONe','DOne','Done','dONE','doNE','donE','DoNe','DoNE','DonE','dOne','dONe','dOnE','doNe','DOnE','DoNE','DoNe']:
                list = []
                list.append(toppings)
                return toppings
            elif toppings not in ['E','e','M','m','G','g','T','t','P','p','F','f','K','k','B','b','A','a','I','i','H','h','F','f']:
                print("That is not a valid input. Try again.")




def sizeMenu():
    while True:
            size = input("What size pizza do you want? (S)mall, (M)edium, or (L)arge ")
            if 'S' == size or 's' == size:
                return size
            elif 'M' == size or 'm' == size:
                return size
            elif 'L' == size or 'l' == size:
                return size
            else:
                print("That is not a size we have. Try again")
#I used the below site/code to help me in developing an order numbering system
#https://stackoverflow.com/questions/42350029/assign-a-number-to-each-unique-value-in-a-list
def curstMenu():
    while True:
        try:
            curst = input("What curst do you want? (H)and-tossed, (T)hin, (C)heese Stuffed or (D)eep Dish ")
            if 'H' == curst or 'h' == curst:
                return curst
            elif 'T' == curst or 't' == curst:
                return curst
            elif 'C' == curst or 'c' == curst:
                return curst
            elif 'D' == curst or 'd' == curst:
                return curst
            else:
                print("That is not a crust we have. Try again")
        except:
            break

def printBeginning():
    print('Welcome to Pie in the Sky Pizza Shoppe!')
    print("(O)rder a pizza")
    print("(F)inish an order")
    print("(D)isplay un-finished orders")
    print("(E)xit")



def main():
    finishList1 = []
    finishList = []
    orderdetails = []
    allunfinished = []
    while True:
        try:
            
            printBeginning()
            userInput = input()
            if 'O' == userInput or 'o' == userInput:
                #orderdetails = []
                size = sizeMenu()
                curst = curstMenu()
                sauce = sauceMenu()
                toppings = toppingMenu()
                p1 = Pizza(size, curst, sauce, toppings,done=False)
                allunfinished.append(p1)
                orderdetails.append(p1)
                count = 0
                while count < len(orderdetails):
                    count = count + 1
                print('This order number is {}'.format(count))
            elif 'F' == userInput or 'f' == userInput:
                while True:
                    try:

                        orderNumber = eval(input('Please enter the order number: '))
                        orderdetails[orderNumber - 1].done=True
                        break
                    except:
                        print('That is not a valid order number. Try again')
            elif 'D' == userInput or 'd' == userInput:
                try:
                    count = 0
                    countTrue = []
                    countFalse = []
                    #if count == 0:
                    #    print('All orders complete')
                #for the functionality of displaying the index of the list containing the class I used an enumerate fucntion i Learned from the website listed below:
                    #https: // stackoverflow.com / questions / 364621 / how - to - get - items - position - in -a - list
                    ''' gen = (i for i, x in enumerate(orderdetails) if x.done == False)

                        #for i in (i for i, x.done in enumerate(orderdetails) if x.done == False):
                    for i in gen:
                        x =1
                        print(i+1, 'is not complete.')
                        countFalse.append(i)'''

                    for i in range(len(orderdetails)):
                        if orderdetails[i].done == False:
                            print(i+1,'is not complete.')
                            count+= 1
                        if orderdetails[i].done == True:
                            pass

                    if count == 0:
                       print('All orders complete')

                except TypeError:
                    #if all true an error type occurs, so i included an exception to print it ot since itll override the error
                    print('All orders complete')

            elif 'E' == userInput or 'e' == userInput:
                break
            elif userInput != ['O','o','F','f','D','d','E','e']:
                print('Type an O, F, D, or E')
        except:
            pass


main()
