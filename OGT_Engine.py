#import OGT_PeripherialManagement as PM_OGT
#import OGT_Scheduling as S_OGT
#import OGT_GPIO as G_OGT

#from GPTKivy2 import KivyApp
import OGT_Bay
import OGT_FileIO

import pandas as pd
from json import loads, dump
#import datetime as dt
import time
#import logging as LG
#import OGT_Kivy as KV

"""def StartLogging():
    LG.basicConfig(filename="GPIO.log",level=lg.DEBUG,filemode="a+",format="%(asctime) %(levelname) ")
"""



if __name__ == "__main__":
    print("Welcome to OGT")
    time.sleep(2)
    print("Let's get started....")
    Test1=False
    Test2=True
    
    
    """
    if Test1 ==True:
        KApp=KivyApp()
        KApp.run()
    """
            
    if Test2==True:
        df = pd.DataFrame.from_dict(OGT_Bay.Tent.Test_Data())

        # Changing the headers
        df.columns = OGT_Bay.Tent.Tent_As_Header()
        # Writing the DataFrame to a CSV file
        df.to_csv("test.csv", index=False)
        # Extracting the schema from the DataFrame and writing it to a JSON file
        schema = loads(df.to_json(orient='table'))
        with open("schema.json", "w") as fp:
            dump(schema, fp)