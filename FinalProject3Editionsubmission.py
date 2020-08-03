def main():
    #Add a print statement that forces the input onto a new line
    while (True):
        try:
            user_input, secret_word, message = input("").split(";")
            #secret_word = input("")
            alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
            alphabet1 = []
            
            if int(str(user_input)) < 0:
                #print("Invalid Number") #To check this if statement works
                break
    
            '''for n in range(len(alphabet) - (int(str(user_input))), len(alphabet)):
                alphabet1.append(alphabet[n])
            for n in range(0, len(alphabet) - int(str(user_input))):
                alphabet1.append(alphabet[n])
            for i in range(len(alphabet)):
                i = i+1'''
                #print(i, end = " ")
            #print(alphabet1)

            for n in range((len(alphabet) - int(str(user_input))) % 26, len(alphabet)):
                #num = int(str(alphabet))%26
                #alphabet1.append(num)
                alphabet1.append(alphabet[n])
            for n in range(0,(len(alphabet) - int(str(user_input))) % 26):
                alphabet1.append(alphabet[n])
            #for i in range(len(alphabet)):
               # i = i+1

        #Secret Word Code Portion
            secret_word = secret_word.lower()
            conversion = []
        #Secret Word Letter to Number
            for character in secret_word:
                if int(str(user_input)) > 0:#remove if not working (next two lines)
                    number = ((ord(character) - 96 + int(str(user_input)))%26)
                    conversion.append(number)
                if int(str(user_input)) == 0:
                    number = ord(character) - 96 + int(str(user_input))
                    conversion.append(number)
            #print(conversion)
    
    
    #Extending the word to the size:
            extend = []
            extendList = []
            aList = []
    
            for x in range(0, len(message)):
                extend.extend((secret_word))
                #print(extend[x], end="")
            for x in range(0, len(message)):
                extendList.extend((conversion))
                aList.append(extendList[x])
                #print((extendList[x]),end=",")

            #print(aList)
    
    #Conversions of extended message/secret word
            message = message.replace(" ", "")
            message = message.lower()
            #print(message)
            extendConversion = []
    
    #Converting the newly extended word from letter to numbers using a shift (>=0)
            for ch in message:
                if int(str(user_input)) > 0:#remove if not working (next five lines)
                    numMessage = ((ord(ch) - 96 + int(str(user_input)))%26)
                    extendConversion.append(numMessage)
                if int(str(user_input)) == 0:
                    numMessage = ord(ch) - 96 + int(str(user_input))
                    extendConversion.append(numMessage)
    

            #print(extendConversion, end="")
    
    
    #Shift the secret word from the message:
            new_shiftList = []
            shiftList= []
            for x in range(len(extendConversion)):
                shiftList = extendConversion[x] + aList[x]
                new_shiftList.append(shiftList)
                #print(str((shiftList)), end=" ")
            #print(new_shiftList)
    
            new_shiftListconversion = []
    #Secret Word Letter to Number
            for ch in new_shiftList:
                if int(str(user_input)) == 0:
                    while ch > 26:
                        num2 = str(chr((ch%26)+ 96 - int(str(user_input))))
                        num2 = num2.upper()
                        new_shiftListconversion.append(num2)
                        break
                    while ch <= 26:
                        num2 = str(chr(ch+ 96 - int(str(user_input))))
                        num2 = num2.upper()
                        new_shiftListconversion.append(num2)
                        break
                if int(str(user_input))!=0:
                    for i in alphabet1:
                        if ch > 26:
                            num2 = (((ch)%26)-1)
                            num2 = alphabet1[num2]
                            #num2 = (alphabet1[ch])
                            num2 = num2.upper()
                            new_shiftListconversion.append(num2)
                            break

                        if ch <= 26:
                            num2 = (((ch)%26)-1)
                            num2 = alphabet1[num2]
                            #num2 = (alphabet1[ch])
                            num2 = num2.upper()
                            new_shiftListconversion.append(num2)
                            break

                    '''while ch <= 26:
                        num2 = str(chr(ch+ 96 - int(str(user_input))))
                        num2 = num2.upper()
                        new_shiftListconversion.append(num2)
                        break'''

            #print((new_shiftListconversion))

            final_output = []
            for x in range(0, len(new_shiftListconversion)):
                final_output.extend((new_shiftListconversion))
                print(final_output[x], end="")



        except ValueError:
            #print("Value Error")
            break
        except:
            #print("Fail")
            break
        #To Print next inputs into a new line beneath the previous output of the earlier inout
        print()

main()

