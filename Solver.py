#working to create a solver for a path problem, where we read a file and determine if it is solvable or not
#our output will be able to be put into a SAT Solver
#testing git
import os

filename = input("Enter the name of the file you want to read: ")
cwd = os.getcwd()
os.chdir(os.path.join(cwd, 'InputFiles'))
InputFile = open(filename, 'r')
Lines = InputFile.readlines()
InputFileContents = InputFile.read()

#get the number of lines in the .txt file
NumNodes = len(Lines)
print(NumNodes)

