# -*- coding: utf-8 -*-

from AtpTests.Test import Test
#import dft.AtpFileFactory 

class LoadDriveSignalsTest(Test):
    """LoadDriveSignalsTest class, inherits from Test"""
    def __init__(self,atpFileFactory ,doTest):
        """SciTest constructor, takes atpFileFactory and doTest ."""
        Test.__init__( self, atpFileFactory, doTest )
        self.sectionNumber = '6.4'
        
    def __str__( self ):
        """String representation of SciTest"""
        return "%5s%s" % (  Test.__str__( self ),"LoadDrive and Signals")#,self.sectionNumber ) 
    
    def testCriterion(self):
        """testCriterion overrided method from Test abstract class"""
        str='Load Monitor - Test for 48V .Each actual motor will come like (will be 4 blocks like this) '
        #self.atpFileFactory.writeAtp(str)
        #self.atpFileFactory.writeAtp('\n')
        #self.atpFileFactory.writeAtp('_'*len(str))
        
        print(str)
     
    def runTest(self):
        """runTest is overrided method from Test abstract class"""
        #self.atpFileFactory.writeAtp('\n')
        #self.atpFileFactory.writeAtp(self.__str__())
        #self.atpFileFactory.writeAtp('\n')
        self.testCriterion()
        #self.atpFileFactory.writeAtp('\n')
        
        return self.fail
#print(SciTest('f',1))
    
if __name__ == "__main__":
    print ("Hello LoadDriveSignalsTest Test")
    
    