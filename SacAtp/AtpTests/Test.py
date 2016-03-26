# -*- coding: utf-8 -*-
class Test:
    '''Abstract base class Test'''
    def __init__(self, atr ,doTest):
        """Test constructor, takes atpFileFactory and doTest .
             NOTE: Cannot create object of class Test."""
        if self.__class__ == Test:
            raise NotImplementedError \
            ("Cannot create object of class Test")
        self.atr = atr
        self.sectionNumber = ''
        self.fail = False
        self.doTest = doTest
        
        
#    def __setattr__( self, name, value ):
#        """Assigns a value to an attribute"""
#        if name == "doTest":
#            if 0 == value or value == 1:
#                self.__dict__[ "_doTest" ] = value
#            else:
#              raise ValueError, "Invalid doTest value: %d" % value
#        if name == "atpFileFactory":
#            if isinstance(atpFileFactory,aff.AtpFileFactory()):
#                self.__dict__[ "_atpFileFactory" ] = value
#        
    def __str__( self ):
         """String representation of Test"""
         return "" 
    
    def testCriterion(self):
        """Abstract method; derived classes must override"""
        raise NotImplementedError ("Cannot call abstract method")
     
    def runTest(self):
        """Abstract method; derived classes must override"""
        raise NotImplementedError ("Cannot call abstract method" )
        
        
    