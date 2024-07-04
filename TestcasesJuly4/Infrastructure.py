import json
import requests
import logging


class ApiAutomationInfra:
    def __init__(self):
        self.logger = None
        self.token = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def login_valid_user(self):
        url = "https://api.zoomview.ai/saas-auth/api/v1/auth/login"
        body = {
            "email": "anshul.reejonia@zybisys.com",
            "password": "Demo@1234"
        }
        response = requests.post(url, json=body)
        assert response.status_code == 200
        data = response.json()
        self.token = data["message"]["token"]



    def host_details(self):
            url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/host"
            headers = {
                "Authorization": f"Bearer {self.token}"
            }
            response = requests.get(url, headers=headers)
            print(f"API LOADED TIME : ", {response.elapsed.total_seconds()})
            sts_code = response.status_code
            if response.status_code == 200:
                print(f"Status Code is 200")
            else:
                print(f"invalid Status Code {sts_code} is present")

            if response.headers['Content-Type'] == 'application/json; charset=utf-8':
                print(response.headers['Content-type'])
                print(f"valid Header is present")
            else:
                print(f" Invalid Header : {response.headers['Content-Type']} is present")

            Api_load = response.elapsed.total_seconds()
            # ss = str(Api_load)[:4]
            # print(ss)
            print(f"API LOADED TIME : ", {response.elapsed.total_seconds()})
            host_data = response.json()
            # print(host_data)
            formate_data = json.dumps(host_data, indent=4)
            print(f"Host_details DATA :  {formate_data}")
            host_message = host_data["message"]

            for item in host_message:
                print("Host id : ", item['_id'])
                print("Customer Id : ", item['customer_id'])

            self.logger = logging.getLogger()
            self.logger.info("********************** --HOST DETAILS API END-- ******************************")

    def overall_host(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/overall-host-service"
        header = {
            "Authorization":f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        # assert response.status_code == 200
        sts_code = response.status_code
        print(f"API LOADED TIME : ", {response.elapsed.total_seconds()})
        if response.status_code == 200:
            print(f"Status Code is 200")
        else:
            print(f"invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        overall_data = response.json()["message"]
        print(f"overall host data : {overall_data}")

        for status in overall_data:
            print(f"STATUS DATA : {status}")
        print("---")
        self.logger = logging.getLogger()
        self.logger.info("********************** --OVERALL HOST API END-- ******************************")


infra_api = ApiAutomationInfra()
infra_api.login_valid_user()
infra_api.host_details()
infra_api.overall_host()


