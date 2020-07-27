import requests
import json
from ApplicationUtils.CommonUtils.ApplicationLib import ApplicationUtils

class Get(ApplicationUtils):

      def getCategories(self):
        baseURL=self.getEnvironmentDeatils("BASE_URL","URL")
        resources = self.getEnvironmentDeatils("RESOURCES", "CATEGORIES")
        resposne=requests.get(baseURL+resources)
        output=json.dumps(json.loads(resposne.text),indent=4)
        file = open("../OutPut/GetCategories.json", 'w')
        print(output)
        json.dump( json.loads(resposne.text),file,indent=4)
        assert resposne.status_code==200,'Verify the status code is 200, when we try to get the categories'
        print(json.loads(resposne.text)["categories"][0]["name"])
        return json.loads(resposne.text)["categories"][0]["name"]

      def searchCategories(self,categoryID):

        baseURL=self.getEnvironmentDeatils("BASE_URL","URL")
        resources = self.getEnvironmentDeatils("RESOURCES", "CATEGORIES")+categoryID
        print(baseURL+resources)
        resposne=requests.get(baseURL+resources)

        output=json.dumps(json.loads(resposne.text),indent=4)
        file = open("../OutPut/SearchCategories.json", 'w')
        print(output)
        json.dump(json.loads(resposne.text), file, indent=4)
        assert resposne.status_code==200,'Verify the status code is 200, when we try to search the categories'


      def getCustomerByID(self,CustomerID):
        baseURL = self.getEnvironmentDeatils("BASE_URL", "URL")
        resources = self.getEnvironmentDeatils("RESOURCES", "CREATE_CUSTOMER") + CustomerID
        print(baseURL + resources)
        resposne = requests.get(baseURL + resources)

        output = json.dumps(json.loads(resposne.text), indent=4)
        file = open("../OutPut/CustomerDetails.json", 'w')
        print(output)
        json.dump(json.loads(resposne.text), file, indent=4)
        assert resposne.status_code == 200, 'Verify the status code is 200, when we try to search the Customer'



