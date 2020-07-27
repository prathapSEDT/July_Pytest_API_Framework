import  unittest
from ApplicationUtils.CommonUtils.ApplicationLib import ApplicationUtils
import pytest
import allure_pytest
from ApplicationUtils.GET .GET_Lib import Get
import allure

class TC01(unittest.TestCase,ApplicationUtils):

    @allure.severity(severity_level="Critical")
    @allure.story("US12345")
    @allure.feature("Write the name of feature here")
    @pytest.mark.usefixtures("intiateExecutionProcess")
    def test_ValidateSomeThing(self):

        get=Get()
        categoryId=get.getCategories()
        get.searchCategories(categoryId)
