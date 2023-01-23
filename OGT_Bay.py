import OGT_Plant as pl
from pandas import DataFrame

class BayParts:
    baySoilLVL:float
    bayPlant:pl.Plant

class Tent():

    tent_Name  :str
    tent_Length :int
    tent_Width :int
    tent_Height :int
    tent_Total_Wattage :int
    tent_Light_Count :int
    tent_Airflow :bool
    tent_Bay_Count :int
    tent_Bay_Type :str

    @staticmethod
    def Test_Data()->dict:
        return {
        "tent_Name": ["Test Tent"],
        "tent_Length": [20],
        "tent_Width": [10],
        "tent_Height": [8],
        "tent_Total_Wattage": [1000],
        "tent_Light_Count": [20],
        "tent_Airflow": [200],
        "tent_Bay_Count": [5],
        "tent_Bay_Type": ["Double"]
        }
    
    @staticmethod
    def Tent_As_Header() -> list[str]:
            
            return [
            "tent_Name",
            "tent_Length",
            "tent_Width",
            "tent_Height",
            "tent_Total_Wattage",
            "tent_Light_Count",
            "tent_Airflow",
            "tent_Bay_Count",
            "tent_Bay_Type",
            ]



