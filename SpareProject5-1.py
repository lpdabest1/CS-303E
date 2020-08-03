def main():
    inputFile = open('dna.txt','r')
    alist= []
    number_line = inputFile.readline()
    #print(number_line)
    n = int(number_line)
    #print(n)
    numberOfLinesToRead = n*2
    #print(numberOfLinesToRead)
    list = []
    listA=[]
    listB=[]
    firstStrings = []
    secondStrings =[]
    match = str()
    for i in range(numberOfLinesToRead):
        list.append(inputFile.readline().strip('\n'))
    #print(list)

    for i in range(0,len(list),2):
        firstStrings.append(list[i])
        secondStrings.append(list[i+1])
    inputFile.close()
    #print(firstStrings)
    #print(secondStrings)


    #output(n,firstStrings,secondStrings,listA,listB)
    #inp
    #utput(n
    output_File = open('dnaresults.txt','w+')
    pairs(n,firstStrings,secondStrings,listA,listB)
    for i in listA:

        output_File.write(str(i))
    output_File.write('\n')
    for i in listB:
        output_File.write(i)
    output_File.write('\n')

    output_File.close()

# I used the site below to assist me with learning about recursive functions over multiple strings and their length/indices
#https://www.cs.hmc.edu/csforall/FunctionalProgramming/functionalprogramming.html
#https://www.programiz.com/python-programming/methods/built-in/zip
def pairs(n,firstStrings,secondStrings,listA,listB):
    for i, j in zip(firstStrings,secondStrings):
        #print(i)
        #print(j)
        str1 = i
        str2 = j
        str1 = str(str1)
        str2 = str(str2)

        validSequence(str1,str2,listA,listB,n)


#def output(n,firstStrings,secondStrings,listA,listB):
    '''   for i in range(n):
        print('DNA sequence pair '+str(i))
        #pairs(firstStrings,secondStrings,listA,listB)'''


def validSequence(string1,string2,listA,listB,n):

    try:

        for i in range(len(string1)):
            for j in range(len(string2)):
                match = (string1[0] in ['A','a'] and string2[0] in ['T','t']) or (string1[0] in ['T','t'] and string2[0] in ['A','a']) or (string1[0] in ['G','g'] and string2[0] in ['C','c']) or (string1[0] in ['C','c'] and string2[0] in ['G','g'])
                while match is True:
                    #print(string1[0]+string2[0])
                    print(string1[0],end='')
                    print(string2[0],end='')
                    listA.append(string1[0])
                    listB.append(string2[0])
                    return validSequence(string1[1:],string2[1:],listA,listB,n)
                if not match:
                    print()
                    return validSequence(string1[1:],string2[1:],listA,listB,n)
                while string1[-1] and string2[-1]!= match:
                    for k in range(n):
                        print('DNA sequence pair ' + str(k))
    except:
        return validSequence(string1[1:], string2[1:],listA,listB,n)
    print()

main()
