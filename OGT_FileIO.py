

""" File IO Functions
        A) CheckFile
            **            
        B) FIO_DIR
            **            
        C) 
            **            
        D) 
            **            
        E)  
            **
             
"""

#OGT Imports
import OGT_PeripherialManagement as OM
import OGT_UserProfile
import OGT_Testingground_test

#Other Imports
import pandas as pd
from pandas import DataFrame
import os
import logging as lg

Folders = [
    "Maintenence",
    "Logs",
    "Databases",
    "PyApps",
    "KivyFiles",
    "Schema",
    ]

homePath=f"/home/{OGT_UserProfile.USERNAME}/OGT/Helpers/Engine_"
DBPath=homePath+Folders[2] #Folders[2]-->Databases

class DB_Struct:
    """ DBStruct
    This is the base class for interacting with the csv. 
    """        
    DBName:str
    DBHeaders:list[str]=[]
    DBIndexSize:int
    DBColumnTypes:list=[]
    
    DB_SChema={
        "DBName":str,
        "DBHeaders":list[str],
        "DBIndexSize":int,
        "DBColumnTypes":list 
        }   
    def __init__(self,DBName,DBHeaders,DBColumnTypes=[]) -> None:
        self.DBName=DBName
        self.DBHeaders=DBHeaders
        self.DBColumnTypes=DBColumnTypes
    
      
class PDDB(DB_Struct):
    """ PDDB(DB_Struct) -- Pandas Database
        /// Take the perameters for the DB_Struct to access the Database(DB) 
            
            get_DBCSV
                -- Get the Dataframe for the DB you are trying to access
    """        
    def __init__(self,DBName,DBHeaders,DBColTypes):
        super().__init__(DBName,DBHeaders,DBColTypes)
        self.PDCSV=pd.read_csv((DBPath+"/"+DB_Struct.DBName+".csv"),names=DB_Struct.DBHeaders)
        
                
    def get_DBCSV(self) -> DataFrame:
        return self.PDCSV
 
                
    @staticmethod
    def Test_Data():
        return {
        "DBName":"DBTEST",
        "DBHeaders":list[str],
        "DBIndexSize":int,
        "DBColumnTypes":list
        }
    @staticmethod
    def class_As_Header():
        return[
            "DBName",
            "DBHeaders",
            "DBIndexSize",
            "DBColumnTypes"
            ]


class DBDisplay(PDDB):
    """DBDisplay -- Database Display

        /// Special Functions to access the DB 

    Parameters
    ----------
    PDDB
        Print the top rows of the File
    """    
    
    def __init__(self):
        self.db:DataFrame=self.PDCSV

    
    def DISPHead(self) -> DataFrame:
        return self.get_DBCSV().head()

class GIT():
    

class OGT_DIRS(): 
    def __init__(self,wantToLog=True,logFile="FILE_IO") -> None:
        self.wantToLog=wantToLog
        self.logPath=homePath+Folders[1] #Folders[1]-->Logs
        self.logFile=logFile
        if wantToLog == True:
            lg.basicConfig(filename=self.logPath+"/"+self.logFile+".log",filemode="a+",format="%(asctime) -- %(levelname) -- %(message) -- %(stack_info)")
    
    @staticmethod  
    def initiate_DIRS():
        """
        This Function is for the program to create the Folders to put the assets needed for this Project. If if the Folder already exist then the warning will be logged
        
        """
        for dir in Folders:
            new_dir=homePath+dir
            try:                
                os.makedirs(new_dir,exist_ok=False)
            except Exception as OE:
                
            
                msg=f"{new_dir}  already exist"
                lg.warning(OE,exc_info=True,stack_info=True)
                print(msg)    
if __name__ == "__main__":
    OGT_DIRS()
    OGT_DIRS.initiate_DIRS()
    #pass
    



