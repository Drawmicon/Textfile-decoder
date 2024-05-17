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

    for i in range(1,len(wordList)+1):
        counter += 1
        for iter, wrd in enumerate(wordList):
            #print("Number to Find: [", counter, "]  vs numList[", numList[iter], "]", " \nwordList: ", wrd )
            if counter == numList[iter]:
                wordList2.append(wordList[iter])
                numList2.append(numList[iter])

                #print("\t\tWords: ", wordList2)
                #print("\t\tNums: ", numList2)
                break

    return wordList2, numList2


def decoder(file_path_string):

    secretMessage = ""

    file_path = file_path_string
    message = readTXT2String(file_path)
    stringList = stringSplitter(message)
    for x in stringList:
        stringNumberLists(x)
    wordList, numList = reorder()


    print("Num List: ",numList, "\n")
    print("Word List: ",wordList, "\n")

    counter = 0
    iter = 1
    while counter <= len(wordList)-1:
        counter += (iter)
        iter+=1
        secretMessage += wordList[counter-1]
    return secretMessage


secretMessage = decoder("./message_file2.txt")
print (secretMessage)

