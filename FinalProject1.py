
def main():

    print("Hello User! Welcome to the Program!")
    name = str(input("What is your name? "))
    print("Hello, " + str(name))
    favoritenumber = int(input("What is your favorite number? "))
    int_favoritenumber = int(favoritenumber)
    half = int_favoritenumber / 2
    print("Did you know that half of your favorite number "+"(" + str(favoritenumber) + ")"+" is "+str(int(half))+"?")
    print("The program has completed and will exit now.")


main()

