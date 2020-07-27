import  unittest
from ApplicationUtils.CommonUtils.ApplicationLib import ApplicationUtils
from ApplicationUtils.PUT.PUT_Lib import Put
import pytest
import allure_pytest
from ApplicationUtils.GET .GET_Lib import Get
from ApplicationUtils.POST .POST_Lib import Post
from ApplicationUtils.DELETE .DELETE_Lib import  Delete
import allure
import time
class TC02(unittest.TestCase,ApplicationUtils):

    @allure.severity(severity_level="Critical")
    @allure.story("US1345")
    @allure.feature("E2E TestCase Execution")
    @pytest.mark.usefixtures("intiateExecutionProcess")
    def test_ValidateE2ETestCase(self):

        post=Post()
        customerID=post.createCustomer()

        get=Get()
        get.getCustomerByID(customerID)

        put=Put()
        put.updateCustomer(customerID)

        orderID=post.createOrder(customerID)

        time.sleep(3)

        delete=Delete()
        delete.deleteOrder(orderID)