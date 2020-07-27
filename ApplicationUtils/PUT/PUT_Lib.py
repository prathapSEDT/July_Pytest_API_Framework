import requests
import json
from ApplicationUtils.CommonUtils.ApplicationLib import ApplicationUtils

class Put(ApplicationUtils):

      def updateCustomer(self,CutomerID):
        baseURL=self.getEnvironmentDeatils("BASE_URL","URL")
        resources = self.getEnvironmentDeatils("RESOURCES", "CREATE_CUSTOMER")+CutomerID
        jsonInput=open("../Payloads/CreateCustomer.json")

        payload=json.load(jsonInput)
        payload["firstname"] = "Veera Prathap"
        payload["lastname"] = "Malepati"

        resposne=requests.put(baseURL+resources,data=payload)
        output=json.dumps(json.loads(resposne.text),indent=4)
        file = open("../OutPut/Modified_Customer.json", 'w')
        print(output)
        json.dump( json.loads(resposne.text),file,indent=4)
        assert resposne.status_code==200,'Verify the status code is 200, when we try to update a customer'
