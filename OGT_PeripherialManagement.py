from pandas import DataFrame as pDF
import OGT_FileIO as FIO
""" Peripherial Management


    A) UsedPeripherials
        ** The setup and configuration of the devices used in the project
            
    B) PeripherialInput    
        ** Getting the input data
        
    C)  PeripherialOutput 
        ** Setting the state of the peripherial
    
    D) PeripherialStatus
        ** Get informaiton to decipher what the peripherial is doing
    
    E) PeripherialLogging
        ** Logging Issues that would need to be addressed
        """
        

class Peripherial:
    PName:str
    PType:str
    PPin:int
    PFunction:str
    PFilePath:str
    PData:pDF
    PToggle:bool            
    PStatus:str
    PScheduleInfo:str
    
    def __init__(self, Periphrial_name, userModSoil="Normal" ):
        self.PName = Periphrial_name
        self.PType = userModSoil + " Soil"
        
    @staticmethod
    def Test_Data():
        return{
            "PName":"GDP_Mother_1",
            "PType":"Sensor",
            "PPin":4,
            "PFunction":"Humidity",
            "PFilePath":FIO.homePath,
            "PData":FIO.homePath,
            "PToggle":False,
            "PStatus":"Active",
            "PScheduleInfo":"Standard",
            }
    @staticmethod
    def Peripherial_As_Header():
        return[
            "PName",
            "PType",
            "PPin",
            "PFunction",
            "PFilePath",
            "PData",
            "PToggle",
            "PStatus",
            "PScheduleInfo",
                ]

class PeripherialConstraints(Peripherial):
    Pminimum:int
    Pmaximum:int
    def __init__(self, Periphrial_name, userModSoil="Normal"):
        super().__init__(Periphrial_name, userModSoil)
        
    
    

if __name__ == "__main__":           
    
    piph=Peripherial("Grand Daddy Purple")  
    piph.PType="Weed"
    piph.PPin=4
    piph.PToggle                                                                                                                                                        =True
 
    