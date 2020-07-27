import requests
import json
import re

from ApplicationUtils.CommonUtils.ApplicationLib import ApplicationUtils

class Post(ApplicationUtils):

      def createCustomer(self):
        baseURL=self.getEnvironmentDeatils("BASE_URL","URL")
        resources = self.getEnvironmentDeatils("RESOURCES", "CREATE_CUSTOMER")
        jsonInput=open("../Payloads/CreateCustomer.json")
        payload=json.load(jsonInput)

        resposne=requests.post(baseURL+resources,data=payload)
        output=json.dumps(json.loads(resposne.text),indent=4)
        file = open("../OutPut/CreateCustomer.json", 'w')
        print(output)
        json.dump( json.loads(resposne.text),file,indent=4)
        assert resposne.status_code==201,'Verify the status code is 201, when we try to create a customer'

        customerID=str(json.loads(resposne.text)["customer_url"])[str(json.loads(resposne.text)["customer_url"]).rfind("/")+1:]

        print(customerID)
        return customerID

      def createOrder(self,cutomerID):
        baseURL=self.getEnvironmentDeatils("BASE_URL","URL")
        resources = self.getEnvironmentDeatils("RESOURCES", "CREATE_ORDER").replace("replaceme",cutomerID)

        resposne=requests.post(baseURL+resources)
        output=json.dumps(json.loads(resposne.text),indent=4)
        file = open("../OutPut/CreateOrder.json", 'w')
        print(output)
        json.dump( json.loads(resposne.text),file,indent=4)
        assert resposne.status_code==201,'Verify the status code is 201, when we try to create an order to a  customer'

        orderID=re.sub("[^0-9]","",json.loads(resposne.text)["items_url"])
        print(orderID)
        return orderID



