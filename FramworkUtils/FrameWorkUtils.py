from configparser import ConfigParser
import os
# from subprocess import Popen

import allure

class FrameWorkLib():

    def __init__(self):
        self.configur = ConfigParser()

    @allure.step("Load the config files")
    def loadConfigFiles(self):
        print("Loading Configuration file.....!!!")
        path="../Configuration/EnvironmentSettings.cnf"
        self.configur.read(path)
        print("Configuration file is loaded sucessfully...")
        return self.configur

    @allure.step("Create Results folder")
    def createResultFolder(self):
        print("Checking for results folder.....")
        path="../Results"
        if not os.path.exists(path):
            os.mkdir(path)
            print("No Resulst Folder Exist, Created Results Folder")
        print("Results Folder check is completed")

    # def runBatFile(self):
    #     path=os.getcwd()+"\\packages.bat"
    #     process=Popen(path,shell=True)
    #     stdout,stderr=process.communicate()









