
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#import os
#os.chdir('../')
#import LdeAutoAtpSetup as las
import AtpFileProcessing as afp
import AtpTime as tm


class AtpFileFactory():
    '''This class provides functions for creating ,reading and writing text files
    in definite format for Atp procedures
    As well this class provides incapsulation for class AtpFileProcesssing. 
   '''
    def __init__(self,date=None,tester=None,serialNumber=None,sysName = None):
        '''constructor of class AtpFileFactory
        date - instance of  AtpTime class
        tester - string of tester name
        serialNumber - string of EUT serial number
        Note: This constructor should be changed in the future.
        'self.fileName' property would be dynamicly changed adding new argument 
        'filename' 
        (ex.: __init__(self,date=None,tester=None,serialNumber=None,filename=None):
        '''
        self.atpFileProcessing = afp.AtpFileProcessing()
        self.atpTime = tm.AtpTime()
        self.fileName = 'AutoLde_XXXX-XX-XX_XXXX.txt'
        self.date = date
        self.tester = tester
        self.serialNumber = serialNumber
        self.sysName = sysName



    def getFileName(self):
        """getter file name"""
        return self.fileName 
    
    def writeAtp(self,str):
        '''write string to file'''
        self.atpFileProcessing.writeAtp(str)
        
    def readAtp(self):
        '''Read all lines (begin from offset 0) in a file'''
        self.atpFileProcessing.pointToBeginOfFile()
        return self.atpFileProcessing.readAtp()
    
    def closeFile(self):
        '''close file'''
        self.atpFileProcessing.closeFile()
    
    def _generateFileName(self):
        '''assign new formatted value to self.fileName '''
        self.fileName = '%s_%s_%s_SN%s.txt'% \
        (self.sysName,self.atpTime.formatDate(self.atpTime.now()),\
        self.atpTime.formatTime(self.atpTime.now()),\
        self.serialNumber) 
        
    
    def openFile(self,pathName=None):
        ''''open file
        pathName = string of path
        Important: pathName is path to directory where you want 
        to create new file '''
        self._generateFileName()
         
        if  pathName != None:
            self.fileName = pathName + self.fileName 
            
        print('FileFactory openFile-%s'%self.fileName)
        self.atpFileProcessing.openFile(self.fileName)
    
    
    def writeAtpHeader(self):
        '''write Header for Atp file'''
        date = self.date
        serialNumber = self.serialNumber
        if date == None:
            date = 'None'
        if serialNumber == None:
            serialNumber = 'None'    
        self.writeAtp('*'*56)
        self.writeAtp('\n')
        self.writeAtp('* LDE Fully Automatic Hardware ATP%s%s\n'% (" "*21,'*') ) 
        # derive file name from relational path
        fileName = self.fileName[self.fileName.find('AutoLde'):]
        self.writeAtp('* File name =%s%s%s\n'%(fileName,' '*(55-(13+len(fileName))),'*'))
        self.writeAtp('* Date = %s%s%s\n*%s%s\n'% (date,' '*(55-(9+len(date))),'*',' '*54,'*'))
        self.writeAtp('* System Serial Number = %s%s%s\n'% (serialNumber," "*(55-(25+len(serialNumber))),'*') )
        self.writeAtp('*'*56)
        self.writeAtp('\n')
        
    def writeAtpConclusion(self,isFail):
        if isFail:
            self.writeAtp('ATP did not complete successfully. The results are in the file:%s\n'% self.fileName)
        else:
            self.writeAtp('ATP completed successfully. The results are in the file:%s\n'% self.fileName)
           
        
        
if __name__ == "__main__":
    #atpTime = tm.AtpTime()
    aff = AtpFileFactory()
    print(aff.fileName)
    #fileName = 'AtpResults/LDE_%s_%s.txt'% \
    #(atpTime.formatDate(atpTime.now()),las.TestSetup['EUT_SerialNumber'])
   # print(dir(aff))
    aff.openFile()
    aff.writeAtpHeader()