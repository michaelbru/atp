# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "mike"
__date__ = "$06/04/2015 09:08:36$"
from functools import reduce
import time
from datetime import timedelta
import datetime

class AtpTime():
    """
    
    """
    delta=timedelta()
    def convertFromEpocToStructTime(self,secs=None):
        ''' converts to local time. 
        If secs is not provided or None, 
        the current time as returned by time() '''
        return time.localtime(secs)
                
    def convertFromStructTimeToEpoc(self,year=2015,mon=1,day=1,hour=0,min=0,sec=0,wday=0,yday=0,isdst=-1):
        '''convert  From Struct Time To Epoc'''
        struct_time=(year,mon,day,hour,min,sec,wday,yday,isdst)
        '''This is the inverse function of localtime(). Its argument is the struct_time or full 9-tuple'''
        return time.mktime(struct_time)
         
    def now(self):
        '''current time 
           return struct_time '''
        return self.convertFromEpocToStructTime()
    
    def nowEpoc(self):
        '''current time
            return epoc time in seconds'''
        stm = self.now()
        return self.setTime(stm[0],stm[1],stm[2],stm[3],stm[4],stm[5])
        
        
    def delay(self,secs):
        time.sleep(secs)
        
    def setTime(self,year=2015,mon=1,day=1,hour=0,min=0,sec=0):
        '''set time for atp tests'''
        return self.convertFromStructTimeToEpoc(year,mon,day,hour,min,sec)
    
    def getTime(self,secs):
        ''' get time from atp '''
        return self.convertFromEpocToStructTime(secs)
    
    def formatTime(self,struct_time):
        '''Convert a tuple or struct_time representing a time as returned 
        by gmtime() or localtime() to a string as specified by the format argument'''
        return time.strftime("%H_%M_%S", struct_time)
    
    def formatDate(self,struct_time):
        '''Convert a tuple or struct_time representing a time as returned 
        by gmtime() or localtime() to a string as specified by the format argument'''
        return time.strftime("%d-%m-%Y", struct_time)
    
    def formatDateandTime(self,struct_time):
        '''Convert a tuple or struct_time representing a time as returned 
        by gmtime() or localtime() to a string as specified by the format argument'''
        return time.strftime("%d-%m-%Y %H:%M:%S", struct_time)
    
    def secondsToStr(self,t):
        return " %d:%02d:%02d.%03d" % \
        reduce(lambda ll,b : divmod(ll[0],b) + ll[1:],
            [(t*1000,),1000,60,60])
            
    @staticmethod     
    def diffTime(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
#        now = getTime()       
#        tNow=timedelta(days=now[2], seconds=now[6], microseconds=0, milliseconds=0, minutes=now[4], hours=now[3], weeks=0)
        tVal = timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks)
        tempVal = tVal - AtpTime.delta
        AtpTime.delta = tVal
        return tempVal
     
    
    def validateDate(date_text):
        try:
            datetime.datetime.strptime(date_text, '%d-%m-%Y')
        except ValueError:
            raise ValueError("Incorrect data format, should be DD-MM-YYYY")

    def validateDateAndTime(dateTime_text):
        try:
            datetime.datetime.strptime(dateTime_text, "%d-%m-%Y %H:%M:%S")
        except ValueError:
            raise ValueError("Incorrect data format, should be DD-MM-YYYY HH:MM:SS")
  

    def today(self):
         #dt = date.today()
        #self.date = dt.__str__()#ftime("%A, %d. %B %Y %I:%M%p")   
        
         return time.strftime("%A %d %B %Y %I:%M%p")

#    @staticmethod 
#    def wait(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
#        res = AtpTime.diffTime(days, seconds, microseconds, milliseconds, minutes, hours, weeks)
#        self.delay(res.seconds)
    
    
#f = '%4i %%'
#len_to_clear = len(f)+1
#clear = '\x08'* len_to_clear
#print ('Progress in percent:'+' '*(len_to_clear),),
#for i in range(123):
#    print (clear+f % (i*100//123),),
#    time.sleep(0.4)
#input('\nDone')
#
#    # status generator
#def range_with_status(total):
#    """ iterate from 0 to total and show progress in console """
#    n=0
#    while n<total:
#        done = '#'*(n+1)
#        todo = '-'*(total-n-1)
#        s = '<{0}>'.format(done+todo)
#        if not todo:
#            s+='\n'        
#        if n>0:
#            s = '\r'+s
#        print(s, ''),
#        yield n
#        n+=1
#
## example for use of status generator
#for i in range_with_status(10):
#    time.sleep(0.1)
if __name__ == "__main__":
    t = time.process_time()
#do some stuff
    print(t)
    print ("Hello Time")
#time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
#                 tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
#  


#ndex	Attribute	Values
#0	tm_year	(for example, 1993)
#1	tm_mon	range [1, 12]
#2	tm_mday	range [1, 31]
#3	tm_hour	range [0, 23]
#4	tm_min	range [0, 59]
#5	tm_sec	range [0, 61]; see (2) in strftime() description
#6	tm_wday	range [0, 6], Monday is 0
#7	tm_yday	range [1, 366]
#8	tm_isdst	0, 1 or -1; see below
    atpT = AtpTime()
    #tm=time()
    print(atpT.formatTime(atpT.convertFromEpocToStructTime()))
    print(atpT.convertFromEpocToStructTime())
    atpT.delay(1)
    print(atpT.convertFromStructTimeToEpoc(2015,4,15,5,30,0))
    atpT.delay(1)
    print(atpT.convertFromEpocToStructTime(atpT.convertFromStructTimeToEpoc(2015,4,15,5,30,0)))
    print(atpT.formatTime(atpT.convertFromEpocToStructTime(atpT.convertFromStructTimeToEpoc(2015,4,15,5,30,0))))
    
    atpT.delay(1)
    print(atpT.convertFromStructTimeToEpoc(2015,4,15,17,30,0))
    atpT.delay(1)
    print(atpT.convertFromEpocToStructTime(atpT.convertFromStructTimeToEpoc(2015,4,15,17,30,0)))
    
    print(atpT.formatDateandTime(atpT.now()))
    stm = atpT.now()
    print(atpT.setTime(stm[0],stm[1],stm[2],stm[3],stm[4],stm[5]))
    print(atpT.nowEpoc())
    print(atpT.setTime(2015,4,15,5,30,0))
    print(atpT.getTime(atpT.setTime(2015,4,15,5,30,0)))
#    while True:
#        #sys.stdout.write('%s\r' % atpT.formatTime(atpT.now()))
#        print( "\r"),
#        print (atpT.formatTime(atpT.now())),
#        
#        #sys.stdout.write( " " * (78 - len(atpT.formatTime(atpT.now()))) + "\a")
#        #sys.stdout.write(atp.formatTime(atp.now()) )
#        #sys.stdout.write("\r\x1b[K"+atpT.formatTime(atpT.now()))
#       # sys.stdout.flush()
#        atpT.delay(1)
        #sys.stdout.write("\r" * (len(atp.formatTime(atp.now()))))
       ## sys.stdout.flush()
       
    elapsed_time = time.process_time() - t
    print('elapsed time=',elapsed_time)
    
    
    line = "="*40    
    print (line)
    print (atpT.secondsToStr(1000) )
    print (atpT.secondsToStr(atpT.setTime(2015,4,15,5,30,0) ))
    print (atpT.secondsToStr(3355.66) )
    
    print (line)
    d=atpT.diffTime(hours=23,days=0)
    print (d)
    print(d.seconds)