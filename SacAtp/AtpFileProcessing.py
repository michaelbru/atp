# -*- coding: utf-8 -*-
import sys

class AtpFileProcessing():
#    def __init__(self,fileName):
#        self.fileName = fileName
#       
    '''This class incapsulates simple Python IO functions'''    
    def openFile(self,fileName):
        '''Opens a file for input and output. 
        If the file exists, it is truncated. If the file does
        not exist, one is created'''
        try:
            self.file = open(fileName,'w+')
        except IOError as ioex:
            print(sys.stderr, "File could not be opened:", ioex)
            sys.exit( 1 )
            
            
#    def isOpen(self):
#        return self.file.isOpen()
#    
    def writeAtp(self,str):
        '''Read string from file'''
        try:
            self.file.write(str)
        except IOError as ioex:
            print(sys.stderr, "Write could not be processed:", ioex)
            sys.exit( 1 )
            
    def readAtp(self):
        '''Reads lines from the file and returns the lines in a list.
        The method reads to the end of the file.
        return list of lines'''
        try:
            strList=self.file.readlines()
        except IOError as ioex:
            print(sys.stderr, "Read could not be processed:", ioex)
            sys.exit( 1 )
        return strList
    
    def pointToBeginOfFile(self):
        '''start from the beginning
        of the file'''
        self.file.seek( 0, 0 )
            
    def closeFile(self):
        self.file.close()

if __name__ == "__main__":
    afp = AtpFileProcessing()
    afp.openFile('Atp.txt')
    afp.writeAtp("Hello file\n")
    afp.writeAtp("Hello file\n")
    afp.writeAtp("Hello file\n")
    afp.pointToBeginOfFile()
    list = afp.readAtp()
    for line in list:
        print(line)
    
    afp.closeFile()