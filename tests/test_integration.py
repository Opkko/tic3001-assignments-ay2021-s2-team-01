from input import Input
import unittest
import filecmp
import timeit
import time
import sys
import os

dirPath = os.path.dirname(os.path.realpath(__file__))
outputPath = os.path.join(dirPath, "Output1.txt")

class TestCase(unittest.TestCase):
    def test_compareresults(self):
        dirPath = os.path.dirname(os.path.realpath(__file__))

        #test1
        if sys.argv[1] == "Titles1.txt" and sys.argv[2] == "Ignored1.txt" and sys.argv[3] == "Required1.txt":
            filePath = os.path.join(dirPath, "testcases/Test1/Titles1.txt")
            ignoredWordsFilePath = os.path.join(dirPath, "testcases/Test1/Ignored1.txt")
            requiredWordsFilePath = os.path.join(dirPath, "testcases/Test1/Required1.txt")
            outputTestPath = os.path.join(dirPath, "testcases/Test1/Output1.txt")
            self.input = Input(filePath, ignoredWordsFilePath, requiredWordsFilePath)
            self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))

        #test2
        elif sys.argv[1] == "Titles2.txt" and sys.argv[2] == "Ignored2.txt" and sys.argv[3] == "Required2.txt":
            filePath = os.path.join(dirPath, "testcases/Test2/Titles2.txt")
            ignoredWordsFilePath = os.path.join(dirPath, "testcases/Test2/Ignored2.txt")
            requiredWordsFilePath = os.path.join(dirPath, "testcases/Test2/Required2.txt")
            outputTestPath = os.path.join(dirPath, "testcases/Test2/Output2.txt")
            self.input = Input(filePath, ignoredWordsFilePath, requiredWordsFilePath)
            self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))

        #test3
        elif sys.argv[1] == "Titles3.txt" and sys.argv[2] == "Ignored3.txt" and sys.argv[3] == "Required3.txt":
            filePath = os.path.join(dirPath, "testcases/Test3/Titles3.txt")
            ignoredWordsFilePath = os.path.join(dirPath, "testcases/Test3/Ignored3.txt")
            requiredWordsFilePath = os.path.join(dirPath, "testcases/Test3/Required3.txt")
            outputTestPath = os.path.join(dirPath, "testcases/Test3/Output3.txt")
            self.input = Input(filePath, ignoredWordsFilePath, requiredWordsFilePath)
            self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))

        #test4
        elif sys.argv[1] == "Titles4.txt" and sys.argv[2] == "Ignored4.txt" and sys.argv[3] == "Required4.txt":
            filePath = os.path.join(dirPath, "testcases/Test4/Titles4.txt")
            ignoredWordsFilePath = os.path.join(dirPath, "testcases/Test4/Ignored4.txt")
            requiredWordsFilePath = os.path.join(dirPath, "testcases/Test4/Required4.txt")
            outputTestPath = os.path.join(dirPath, "testcases/Test4/Output4.txt")
            self.input = Input(filePath, ignoredWordsFilePath, requiredWordsFilePath)
            self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))

        #test5
        elif sys.argv[1] == "Titles5.txt" and sys.argv[2] == "Ignored5.txt" and sys.argv[3] == "Required5.txt":
            filePath = os.path.join(dirPath, "testcases/Test5/Titles5.txt")
            ignoredWordsFilePath = os.path.join(dirPath, "testcases/Test5/Ignored5.txt")
            requiredWordsFilePath = os.path.join(dirPath, "testcases/Test5/Required5.txt")
            outputTestPath = os.path.join(dirPath, "testcases/Test5/Output5.txt")
            self.input = Input(filePath, ignoredWordsFilePath, requiredWordsFilePath)
            self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))
        
        #test6
        elif sys.argv[1] == "Titles6.txt" and sys.argv[2] == "Ignored6.txt" and sys.argv[3] == "Required6.txt":
            filePath = os.path.join(dirPath, "testcases/Test6/Titles6.txt")
            ignoredWordsFilePath = os.path.join(dirPath, "testcases/Test6/Ignored6.txt")
            requiredWordsFilePath = os.path.join(dirPath, "testcases/Test6/Required6.txt")
            outputTestPath = os.path.join(dirPath, "testcases/Test6/Output6.txt")
            self.input = Input(filePath, ignoredWordsFilePath, requiredWordsFilePath)
            self.assertTrue(filecmp.cmp(outputPath, outputTestPath, shallow=False))

        else:
            raise Exception('File(s) not found')

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)