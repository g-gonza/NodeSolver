#working to create a solver for a path problem, where we read a file and determine if it is solvable or not
#our output will be able to be put into a SAT Solver
import os 
import array

#lowercase letters corresponding to numbers starting with 1
Letters = [{'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6,
           'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12,
           'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18,
           's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24,
           'y':25, 'z':26}]

filename = input("Enter the name of the file you want to read: ")
cwd = os.getcwd()
os.chdir(os.path.join(cwd, 'InputFiles'))
InputFile = open(filename, 'r')
Lines = InputFile.readlines()
InputFileContents = InputFile.read()

#get the number of lines in the .txt file
NumNodes = len(Lines)
#print(NumNodes)

#creating a dictionary index for each node
#gonna do some sacrilige by making the index start at 1
VerticeDictionary = {}
VerticeConnections = {}
Num = 1
for i in range(1, NumNodes+1):
    #each node will have a list containing 3 values, going up from 1
    VerticeDictionary[i] = []
    #insert 3 numbers into the list, going up by 1 each time
    for j in range(1, 4):
        VerticeDictionary[i].append(Num)
        Num+=1

for i in range(1, NumNodes+1):

    VerticeConnections[i] = []
    #append each letter from each line to the VerticeConnections dictionary
    for letter in Lines[i-1]:
        if letter != '\n' and letter != ' ':
            VerticeConnections[i].append(letter)

#loop through the VerticeConnections dictionary and convert each letter to its corresponding number from the Letters dictionary
for i in range(1, NumNodes+1):
    for j in range(0, len(VerticeConnections[i])):
        VerticeConnections[i][j] = Letters[0][VerticeConnections[i][j]]

#okay that took awhile



for i in range(1, NumNodes+1):
    String = " ".join(str(x) for x in VerticeDictionary[i])
    print(String + " 0")
    for j in range(0, 3):
        for k in range(j+1, 3):
          print("-" + str(VerticeDictionary[i][j]) + " -" + str(VerticeDictionary[i][k]) + " 0")


#okay, that also took awhile, making simple sets was a pain
#print out the VerticeDictionary entry for each index in VerticeConnections
#for ConnectionVertIndex in range(1, len(VerticeConnections)+1):
#    ConnVert = VerticeConnections[ConnectionVertIndex]
 #   ConnVertLength = len(ConnVert)
#
  #  for ConnNodeIndex in range(0,ConnVertLength-1):
  #      ConnNodeValue = ConnVert[ConnNodeIndex]
   #     for ColorIndex in range(0,3):
    #        Color1Value = VerticeDictionary[ConnectionVertIndex][ColorIndex]
    #        Color2Value = VerticeDictionary[ConnNodeValue][ColorIndex]
#
     #       print("-" + str(Color1Value) + " -" + str(Color2Value) + " 0")



ColorLength = 3
printedCombinations = set()

for ConnVertIndex in range(1, len(VerticeConnections)+1):
    ConnVert = VerticeConnections[ConnVertIndex]
    ConnVertLength = len(ConnVert) 
    for ConnNodeIndex in range(0, ConnVertLength):
        ConnNodeValue = ConnVert[ConnNodeIndex]
    
        for ColorIndex in range(0, ColorLength):
            ColorValue1 = VerticeDictionary[ConnVertIndex][ColorIndex]
            ColorValue2 = VerticeDictionary[ConnNodeValue][ColorIndex]
            
            combination = tuple(sorted([-ColorValue1, -ColorValue2, 0]))
            
            if combination not in printedCombinations:
                printedCombinations.add(combination)
                print(*combination)

#had to use sets instead of lists so that way I could do easy comparisons
            


#print(VerticeDictionary)
#print(VerticeConnections)




    

#print(VerticeDictionary)


