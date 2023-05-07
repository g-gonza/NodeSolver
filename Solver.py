#working to create a solver for a path problem, where we read a file and determine if it is solvable or not
#our output will be able to be put into a SAT Solver
#this deals with the 3-coloring problem
import os 

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

for i in range(1, NumNodes+1):
    String = " ".join(str(x) for x in VerticeDictionary[i])
    print(String + " 0")
    #






    

#print(VerticeDictionary)


