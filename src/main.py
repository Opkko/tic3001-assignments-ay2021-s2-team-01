import os
from input import Input
import sys

def main():
    dirPath = os.path.dirname(os.path.realpath(__file__))
    filePath = os.path.join(dirPath, sys.argv[1])
    ignoredWordsFilePath = os.path.join(dirPath, sys.argv[2])
    requiredWordsFilePath = os.path.join(dirPath, sys.argv[3])

    Input(filePath, ignoredWordsFilePath, requiredWordsFilePath)
  
if __name__== "__main__":
  main()