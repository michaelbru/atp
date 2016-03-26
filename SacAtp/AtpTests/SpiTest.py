# -*- coding: utf-8 -*-

from AtpTests.Test import Test
#import dft.AtpFileFactory 

class SpiTest(Test):
    """SpiTest class, inherits from Test"""
    def __init__(self,atpFileFactory ,doTest):
        """SciTest constructor, takes atpFileFactory and doTest ."""
        Test.__init__( self, atpFileFactory, doTest )
        self.sectionNumber = '6.3'
        
    def __str__( self ):
        """String representation of SciTest"""
        return "%5s%s" % (  Test.__str__( self ),"Spi")#,self.sectionNumber ) 
    
    def testCriterion(self):
        """testCriterion overrided method from Test abstract class"""
        str='Spi Success criterion:  Send command via SPI to each axis of LDE and get response from it.'
        
        #self.atr.writeAtp(str)
        #self.atr.writeAtp('\n')
        #self.atr.writeAtp('_'*len(str))
        
        print(str)
     
    def runTest(self):
        """runTest is overrided method from Test abstract class"""
        #self.atr.writeAtp('\n')
        #self.atr.writeAtp(self.__str__())
        #self.atr.writeAtp('\n')
        self.testCriterion()
        #self.atr.writeAtp('\n')
        return self.fail
#print(SciTest('f',1))
    
if __name__ == "__main__":
    print ("Hello SPI Test")
    
    