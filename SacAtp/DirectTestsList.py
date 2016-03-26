from tkinter import *
import Pmw
import datetime
import AtpTime
import AtpFileFactory
from AtpTests.SciTest import *
from AtpTests.SpiTest import *
from AtpTests.VoltMonitorTest import *
from AtpTests.LoadDriveSignalsTest import *

class Dummy: pass
var = Dummy()
path = 'AtpResults/'
function_table = [ SciTest,SpiTest,LoadDriveSignalsTest,VoltMonitorTest]
tests = [
            ('Spi', 0,0,NORMAL), ('Sci', 1,0,NORMAL),
            ('VoltMonitor', 2,0,NORMAL), ('LoadDriveSignals', 3,0,NORMAL),
            ('Test5',0,1,NORMAL), ('Test6', 1,1,NORMAL)
            ]

def runAtp(tests):
    selectedTests = [x for x in tests if x.doTest==1]  
    if selectedTests == []:
        print('No selected tests')
        return  
    print(selectedTests)
    failTest = False
    
     # unselected tests
    unselectedTests = set(tests)- set(selectedTests)
    print(unselectedTests)
    
    #run selected tests
    for test in selectedTests:
       failTest|=test.runTest()
    
    # write Atp conclusion to file
    #aff.writeAtpConclusion(failTest)
    
    # write unselectedTests to file
    if len(unselectedTests)>0:
        print('The following tests were not selected:\n')
        #aff.writeAtp('The following tests were not selected:\n')
        for ut in unselectedTests:
            #aff.writeAtp(ut.__str__())
            #aff.writeAtp('\n')
            print(ut.__str__())
    if failTest:
        failedTests = [x for x in selectedTests if x.fail==1]
        if len(failedTests)>0:
            #aff.writeAtp('The following tests were failed:\n')
            print('The following tests were failed:\n')
            for ft in failedTests:
                #aff.writeAtp(ft.__str__())
                print(ft.__str__())
                #aff.writeAtp('\n')
           
    # close Atp file
   # aff.closeFile()

class Atr:
    def __init__():
        pass

class AtpForm:
    def __init__(self,sysName=None,tester=None,date=None,eutPn=None,atrFileName=None):
        self.sysName = sysName
        self.tester = tester
        self.setDate(date)
        self.eutPn =eutPn if eutPn!=None else '' 
        self.setFileName(atrFileName)

    def setDate(self,date = None): 
        atpT = AtpTime.AtpTime()
        if date==None:         
            self.date = atpT.today()
        else:
            try:
                atpT.validateDateAndTime(date)
                self.date = date
            except ValueError as ve:
                print(ve)
   
    def setFileName(self,atrFileName=None): 
        '''creates file name 
        :param sysName: The string name of tested System (EUT)
        :param sn : The string of serial number of the tested unit'''    
        if  atrFileName == None:
            aff = AtpFileFactory.AtpFileFactory(serialNumber = self.eutPn,sysName = self.sysName)
            aff._generateFileName()
            file = aff.getFileName() 
            self.atrFileName = file[:file.find('.')]
        else:
            self.atrFileName = atrFileName
        #if ( '.' not in fname):
        #        fname += '.xlsx' 
        #self.atr.setRsltFile( RESULT_TESTS_DIR + fname )


class AtpGui(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        Pmw.initialise()
        self.option_add('*Entry*background',     'lightblue')
        self.option_add('*font',   ('agaramond', 10, 'bold'))
       # self.createGui()
        self.root = master
        self.atpFormObj = AtpForm(sysName = 'SacSimulator',tester = 'Shira',eutPn = 1)
        self.makeAtpForm()
        self.makeTestForm()
        self.makeButtonPanel()
        self.choosedTests = {}
    #Tester Name
    #Test date
    #SN
    def makeAtpForm(self):
        '''create upper form'''       
        self.atpFormFrame=Frame(self, borderwidth=1, relief=GROOVE)
        atpFormGroup = Pmw.Group(self.atpFormFrame, tag_text='Atp Form')
        # date
        self.dateFrame=Frame(atpFormGroup.interior(), borderwidth=1)
        self.content = StringVar()
        Label(self.dateFrame, text='Date', width=10, anchor=W, font=('memorandum', 10, 'bold')).\
            pack(side=LEFT, expand=NO, fill=BOTH)
        self.dateEntry = Entry(self.dateFrame, width=40,name = 'date',textvariable =self.content)
        self.dateEntry.pack(side=RIGHT, expand=YES, fill=BOTH)   
        self.date = self.atpFormObj.date
        self.dateEntry.insert(0 , self.date)
       
        self.dateFrame.pack(side=TOP, expand=YES, fill=BOTH, padx=8, pady=6)
        # tester
        self.testerNameForm=Frame(atpFormGroup.interior(), borderwidth=1)
        Label(self.testerNameForm, text='Tester Name', width=10, anchor=W, font=('memorandum', 10, 'bold')).\
        pack(side=LEFT, expand=NO, fill=BOTH)
        self.testerEntry = Entry(self.testerNameForm, width=40,name = 'tester')
        self.testerEntry.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.testerEntry.insert(0 ,  self.atpFormObj.tester)
        
        self.testerNameForm.pack(side=TOP, expand=YES, fill=BOTH, padx=8, pady=6)
        # serial number
        self.eutsnFrame=Frame(atpFormGroup.interior(), borderwidth=1)
        Label(self.eutsnFrame, text='EUT S/N', width=10, anchor=W, font=('memorandum', 10, 'bold')).\
        pack(side=LEFT, expand=NO, fill=BOTH)
        self.eutSnEntry = Entry(self.eutsnFrame, width=40,name = 'eut')
        self.eutSnEntry.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.eutSnEntry.insert(0 , self.atpFormObj.eutPn)
        
        self.eutsnFrame.pack(side=TOP, expand=YES, fill=BOTH, padx=8, pady=6)
        #file name
        self.fileNameFrame=Frame(atpFormGroup.interior(), borderwidth=1)
        Label(self.fileNameFrame, text='Atr file', width=10, anchor=W, font=('memorandum', 10, 'bold')).\
            pack(side=LEFT, expand=NO, fill=BOTH)
        self.atrFileEntry = Entry(self.fileNameFrame, width=40,name = 'fileName')
        self.atrFileEntry.pack(side=RIGHT, expand=YES, fill=BOTH)
        self.atrFileEntry.insert(0 ,self.atpFormObj.atrFileName )
       
        self.fileNameFrame.pack(side=TOP, expand=YES, fill=BOTH, padx=8, pady=6)

        atpFormGroup.pack()
        self.atpFormFrame.pack(side=TOP, expand=YES, fill=BOTH, padx=8, pady=6)
       

    def makeTestForm(self):
        '''create test form'''
        self.testsForm=Frame(self, borderwidth=1, relief=GROOVE)
        atpTestsFormGroup = Pmw.Group(self.testsForm, tag_text='Tests')
        self.frc=Frame(atpTestsFormGroup.interior(), borderwidth=1)
        #self.__assignTests()
        for testName, row, col, status in tests: 
            setattr(var, testName, IntVar())
            Checkbutton(self.frc, text=testName, state=status, anchor=W,
              variable = getattr(var, testName)).grid(row=row, column=col, sticky=W,padx=5)
        self.frc.pack(side=TOP, expand=YES, fill=BOTH, padx=8, pady=6)
        atpTestsFormGroup.pack( expand=YES, fill=BOTH)
        self.testsForm.pack(side=TOP, expand=YES, fill=BOTH, padx=8, pady=6)

       
    def makeButtonPanel(self):
        '''create buttons form'''
        self.buttonsFrame=Frame(self, borderwidth=0)#, relief=GROOVE)      
        self.clearTestsButton = Button(self.buttonsFrame, text='Clear All', command=self.clearAll, font=('memorandum', 10, 'bold'))
        self.clearTestsButton.pack(side = LEFT,expand=NO, fill=Y, anchor = 'w',padx=20)
        self.checkAllTestsButton= Button(self.buttonsFrame, text='Check All', command=self.checkAll, font=('memorandum', 10, 'bold'))
        self.checkAllTestsButton.pack(side = LEFT,expand=NO, fill=Y, anchor = 'w',padx=20)
        self.runTestsButton = Button(self.buttonsFrame, text='Run Tests', command=self.runTests, font=('memorandum', 10, 'bold'))
        self.runTestsButton.pack(side = RIGHT,expand=NO, fill=Y, anchor = 'w',padx=20)
        self.buttonsFrame.pack(side=TOP, expand=YES, fill=BOTH, padx=1, pady=6)

    def checkAll(self):
         ''' select all tests on test form'''
         for testName, row, col, status in  tests : 
            getattr(var, testName).set(1)

    def clearAll(self):
         ''' clear all tests on test form'''
         for testName, row, col, status in tests  :
            getattr(var, testName).set(0)

    def getSelectedTests(self):
        for testName, row, col, status in  tests : 
            self.choosedTests[testName] = getattr(var, testName).get()

    def getFormAtp(self):
        #print(self.atrFileEntry.get())
        self.atpFormObj.atrFileName = self.atrFileEntry.get()
        self.atpFormObj.eutPn = self.eutSnEntry.get()
        self.atpFormObj.tester = self.testerEntry.get()
        
        
    def runTests(self):
        # 
        from subprocess import call
        import IPython
        from IPython import embed
       
       # IPython.start_ipython(argv=[])
        self.getFormAtp()  
        self.getSelectedTests()
        #close gui
        self.root.destroy()
        #run tests
        print("run tests")           
        print(self.choosedTests)
        self.initTests()
        #embed( )
        runAtp(self.tests)
        #call('ipython notebook ')#ipython nbconvert notebook.ipynb


    def initTests(self):
        self.tests = [ f(None,self.choosedTests[f.__name__[:-4]]) for f in function_table]


    def main(self):
         root = Tk()
         #root.option_readfile('optionDB')
         root.title('Atp')
         gui = AtpGui(root)
         gui.pack()
         root.mainloop()

if __name__=="__main__":
    root = Tk()
    #root.option_readfile('optionDB')
    root.title('Atp')
    gui = AtpGui(root)
    gui.pack()
    root.mainloop()

