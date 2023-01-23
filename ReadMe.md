ReadMe

    ## Description
        Thanks for checking out this project to manage your grow tent. The purpose of this project is to have an easy way to control your Grow Tent. At this time the project is in the initial development, and the team behind the project is only doing this as a hobby and isn't intended to be fully maintained.



    ## Development
        Check the resources to join the Discord if you want to help. Come join us as we build the project. 

        Clone the project

        git clone https://git.com/aceaj12/OGT


    ## Project Files
        Let me explain what the files and folders are going to be used for. It is important for seperation of the individual parts that control what is happening in the project for clarity of each function
        
        
        ### Project Folders
        /bin
        /lib
        /lib64
        /share
            DO NOT TOUCH THESE UNLESS YOU KNOW WHAT YOU ARE DOING 
            -- These are the folders are used to maintain the Python and its dependancies
        
        /Helpers
            -- The Folders here are used for Input and Output of any Reading or Writing of the OGT modules

            OGT/Helpers/Engine_Databases
                -- CSV Files Controlled by Pandas
            OGT/Helpers/Engine_KivyFiles
                -- Assets for the UI
            OGT/Helpers/Engine_Logs
                -- Logs taken from any of the modules
            OGT/Helpers/Engine_Maintenence
                -- Debug and Testing                 
            OGT/Helpers/Engine_Schema
                -- The Profile 

        ___________________________
        ###  Project Python Files

        OGT/OGT_Engine.py
            -- The main way of interacting when controlling the project
        OGT/OGT_Bay.py
            -- This may go away but for now this is for code related to controlling and getting data from each plant
        OGT/OGT_FileIO.py
            -- Controlling the reading and writing to the DBs
        OGT/OGT_GPIO.py
            --Interacting with the pins
        OGT/OGT_Kivy.py
            -- The UI
        OGT/OGT_PeripherialManagement.py
            -- Sensor Data IO management
        OGT/OGT_Plant.py
            -- Manage the commands and status of the plant.        
        OGT/OGT_Scheduling.py
            -- Different schedules for different reasons
        OGT/OGT_Testingground_test.py
            -- Test that need to be run 
        OGT/OGT_UserProfile.py   
            -- Profile for the person whether they are a developer or just a user