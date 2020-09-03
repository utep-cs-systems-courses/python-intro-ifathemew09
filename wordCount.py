#Casey Caiza
#9/1/2020
#This program sorts and counts occurences of words in a given input file.

import re
import sys

inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

with open (inputFileName, "r") as inputFile:
    numWords = dict()
    for line in inputFile:
        line = line.lower()
        line = line.replace('-', " ")
        line = line.replace("'", " ")
        line = re.sub('[^\w\s]', '', line)
        words = line.split()
        for word in words:
            if word not in numWords:
                numWords[word] = 0
            numWords[word] += 1


with open (outputFileName, "w") as outputFile:
    for key, count in sorted(numWords.items()):
        outputFile.write(str(key) + " "+ str(count) + "\n")

        
outputFile.close()
                     
