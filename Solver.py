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

#filename = input("Enter the name of the file you want to read: ")
filename = 'input_graph_1.txt'
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
Num = 1
for i in range(1, NumNodes+1):
    #each node will have a list containing 3 values, going up from 1
    VerticeDictionary[i] = []
    #insert 3 numbers into the list, going up by 1 each time
    
    for j in range(1, 4):
        VerticeDictionary[i].append(Num)
        Num+=1


VerticeConnections = {}
for i in range(1, NumNodes+1):
   
   LetterList = Lines[i-1].split()
   VerticeConnections[i] = LetterList
   

print(VerticeDictionary)
print(VerticeConnections)

for i in range(1, NumNodes+1):
    String = " ".join(str(x) for x in VerticeDictionary[i])
    print(String + " 0")
    






    

#print(VerticeDictionary)


