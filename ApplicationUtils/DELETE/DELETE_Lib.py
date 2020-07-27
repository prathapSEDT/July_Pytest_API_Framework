import requests
import json
import re

from ApplicationUtils.CommonUtils.ApplicationLib import ApplicationUtils

class Delete(ApplicationUtils):

      def deleteOrder(self,orderID):
        baseURL=self.getEnvironmentDeatils("BASE_URL","URL")
        resources = self.getEnvironmentDeatils("RESOURCES", "DELETE_CUSTOMER").replace("replaceme",orderID)
        print(resources)
        resposne=requests.delete(baseURL+resources)
        assert resposne.status_code==200,'Verify the status code is 200, when we try to delete'


