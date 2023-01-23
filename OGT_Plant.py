



class Plant:
    PLName:str
    PLSoilType:str
    
    def __init__(self,PLName:str,PLSoilType:str):
        self.PLName=PLName
        self.PLSoilType=PLSoilType
        
        
    
class Constraints(Plant):
    PCMoisture_min:float
    PCMoisture_max:float
    PCHumidity_min:float
    PCHumidity_max:float
    PCTemperature_min:float
    PCTemperature_max:float
    def __init__(self, PLName: str, PLSoilType: str):
        super().__init__(PLName, PLSoilType)
    
    
    @staticmethod
    def Test_Data() -> dict[str, float]:
        return{
        "PCMoisture_min":69.9,
        "PCMoisture_max":696.9,
        "PCHumidity_min":69.69,
        "PCHumidity_max":969.9,
        "PCTemperature_min":69.69,
        "PCTemperature_max":969.6,
        }
    @staticmethod
    def Constraints_As_Header() -> list[str]:
        return[
        "PCMoisture_min",
        "PCMoisture_max",
        "PCHumidity_min",
        "PCHumidity_max",
        "PCTemperature_min",
        "PCTemperature_max",
        ]
    
if __name__ == "__main__":
    newPlant=Plant("MyGirl_Test","Soil")
    