import os #directory access
import re #regular expression
import sys #sys.exit()

numList = []
wordList = []

#READ A TEXT FILE FROM A FILE PATH AND CONVERT THE TEXT INTO A STRING
def readTXT2String(file_path):
    stringMessage = ""

    with open(file_path, 'r') as file:
        stringMessage = file.read()

    #print("READING FILE...\n", stringMessage)

    return stringMessage

#SPLIT A STRING BY THE NEWLINE CHARACTER INTO MULTIPLE STRINGS
def stringSplitter(message_string):
    s = message_string
    stringList = s.split('\n')
    #print ("\n\n\n\nSPLIT STRING INTO MULTIPLE STRINGS...\n", stringList)
    return stringList



#TAKE THE STRING AND NUMBER VALUES IN A STRING AND ADD IT TO TWO SEPARATE LISTS
def stringNumberLists(stringWithNumber):
    codeNum = int(re.search(r'\d+', stringWithNumber).group())
    result = ''.join([i for i in stringWithNumber if not i.isdigit()])

    numList.append(codeNum)
    wordList.append(result)

    #print("\n\n\nEXTRACT NUM AND STRING...\n", codeNum, ", ", result)


#REORDERS LIST OF WORDS AND NUMBERS IN NUMERICAL ORDER
def reorder():
    numList2 = []
    wordList2 = []

    counter = 0

    for i in range(1,len(wordList)):
        counter += 1
        for iter, wrd in enumerate(wordList):
            #print("Number to Find: [", counter, "]  vs numList[", numList[iter], "]", " \nwordList: ", wrd )
            if counter == numList[iter]:
                wordList2.append(wordList[iter])
                numList2.append(numList[iter])

                print("\t\tWords: ", wordList2)
                print("\t\tNums: ", numList2)
                break

    return wordList2


def decoder(file_path_string):

    secretMessage = ""

    file_path = "/Users/drawmicon/Desktop/Coding/message_file3.txt"
    message = readTXT2String(file_path)
    #print(message)
    stringList = stringSplitter(message)
    #print(stringList)

    for x in stringList:
        stringNumberLists(x)

    wordList = reorder()

    check = 0

    #print("Num List: ",numList, "\n")
    print("Word List: ",wordList, "\n")

    for counter  in range(1, len(wordList)):

        check += counter

        for iterator, word in enumerate(wordList):

            if iterator == check:
                print("counter: ", counter, " \ncheck: ", check, "\nword: ", wordList[iterator], "\n\n")

                secretMessage += wordList[iterator]

                break



    '''
    rowInt = 0
    found  = True
    counter = 0

    secretMessage =""

    while found is True:

        print ("\n\n\t\t\tSecret Message: ", secretMessage, "\n\n")
        rowInt += 1
        counter += rowInt
        found = False

        #print("Row: ", rowInt, " \nCodeNum: ", counter, " \nFound?: ", found, "\n")

        for i, x in enumerate(wordList):
            #print("Current Word: ",wordList[i],"\nInterator: ", i, "\nComparing ", numList[i], " to ", counter)
            if numList[i] == counter:
                print(i, ": ", wordList[i])
                secretMessage += wordList[i]
                found = True
                break

    '''
    return secretMessage


secretMessage = decoder("path")
print (secretMessage)

