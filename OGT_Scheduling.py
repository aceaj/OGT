## Import 
from datetime import datetime as dt
import OGT_PeripherialManagement as PM

""" Scheduling Functions

        A) CalendarYear
            **Using the time and calandar functions to incorporate the higher level functions
            
        B) AutomaticInput
            **When the engine needs to add an event or override an event that it has created 
            
        C) UserOverride
            **When a user needs to override the system to make manual changes to an event
            
        D) TemporaryEvents
            **Events that will last a certain amount of time do to an error or change in operating conditions
            
        E)  LoggingAndFilename
            **Archieved events that need addressing can be found here, and names that require CRUD on directories
             
"""



class Schedule():
    SHName:str
    SHType:str
    SHTimeType:str
    SHAutoSchedule:bool
    SHAppend:bool
    
    @staticmethod
    def Test_Data():
        return{
        "SHName":"Test Schedule",
        "SHType":"24HR",
        "SHTimeType":"Day",
        "SHAutoSchedule":True,
        "SHAppend":True
            }
    
    @staticmethod
    def Schedule_As_Header():
        return[
            "SHName",
            "SHType",
            "SHTimeType",
            "SHAutoSchedule",
            "SHAppend"
            ]
class PEvent(PM.Peripherial):
    PE_Date:dt
    PE_Type:str        


class PowerSchedule():   
    pwr_start:dt
    pwr_end:dt
    pwr_total_On:float
    pwr_run_Time:int
    
    @staticmethod
    def Test_Data():
        return{
        "pwr_start":["2022-01-01 12:00:00"],
        "pwr_end":["2022-01-01 12:00:00"],
        "pwr_total_On":4.5,
        "pwr_run_Time":8}
    
    @staticmethod
    def class_As_Header():
        return[
       "pwr_start",
         "pwr_end",
        "pwr_totalOn",
        "pwr_runTime"
            ]


class AutomaticInput():
    pass

class UserOverride():
    pass

class TemporaryEvents():
    pass

class LoggingAndFilename():
    pass
             
 