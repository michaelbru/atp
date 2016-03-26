# -*- coding: utf-8 -*-

from AtpTests.Test import Test
#import dft.AtpFileFactory 

class VoltMonitorTest(Test):
    """SciTest class, inherits from Test"""
    def __init__(self,atpFileFactory ,doTest):
        """VoltMonitorTest  constructor, takes atpFileFactory and doTest ."""
        Test.__init__( self, atpFileFactory, doTest )
        self.sectionNumber = '6.2'
        
    def __str__( self ):
        """String representation of SciTest"""
        return "%5s%s " % (  Test.__str__( self ),"VoltMonitor")#,self.sectionNumber ) 
    
    def testCriterion(self):
        """testCriterion overrided method from Test abstract class"""
        str = 'Volt monitor Success criterion:    Correct measuring of monitor voltages.'
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
    print ("Hello VoltMonitor Test")
    
    