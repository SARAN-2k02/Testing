import requests
import json
import logging


class ApiAutomationStorage:
    def __init__(self):
        self.token = None
        self.logger = None
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
        # print(self.token)

    def disk_graph(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/disk-graph?host_name=testing&from=1720169229812&to=1720170129812&service_tag=-"
        header = {
            "Authorization": f"bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        sts_code = response.status_code
        print(f" DISK GRAPH API LOADED TIME : {response.elapsed.total_seconds()} seconds")
        if response.status_code == 200:
            print(f"Status code is 200")
        else:
            print(f"Status code {sts_code} Invalid")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        data = response.json()['message']
        format_data = json.dumps(data, indent=4)
        print(f" DISK GRAPH DATA :  {format_data} ")

        print("--------")
        self.logger = logging.getLogger()
        self.logger.info(f"********************** --DISK GRAPH API END-- ******************************")

        # print(response.json(),"SARAN")
    def infra_live_disk(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name=disk"
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        sts_code = response.status_code
        print(f" INFRA LIVE DISK API LOADED TIME : {response.elapsed.total_seconds()} seconds")

        if response.status_code == 200:
            print(f"Status Code is 200")
        else:
            print(f"invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        disk_data = response.json()['message']
        for data in disk_data:
            id = data["_id"]
            customer_id = data['customer_id']
            service_name = data['service_name']

            print(f"Customer Id is {customer_id} is present")
            print(f"Id is {id} is present ")

            if service_name:
                print(f"Service name is present")
            else:
                print("service name not present")

            break

        format_disk_data = json.dumps(disk_data, indent=4)
        print(f" INFRA LIVE DISK DATA : {format_disk_data}")
        self.logger = logging.getLogger()
        self.logger.info("************************************-- INFRA LIVE DISK API END- --**************************")



storage_api = ApiAutomationStorage()
storage_api.login_valid_user()
storage_api.disk_graph()
storage_api.infra_live_disk()
