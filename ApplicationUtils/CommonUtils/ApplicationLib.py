from FramworkUtils.FrameWorkUtils import FrameWorkLib
import pytest
import allure

class ApplicationUtils():
    @pytest.fixture(scope="session")
    def intiateExecutionProcess(self):
        global environment
        obj = FrameWorkLib()
        obj.createResultFolder()
        environment= obj.loadConfigFiles()
        yield
        print("Execution is completed...!!!!")

    @allure.step("Get the Property {1} from the section {0}")
    def getEnvironmentDeatils(self, sectionName, property):
        print("Getting environmenet deatils")
        print(environment.get(sectionName,property))
        return environment.get(sectionName,property)
