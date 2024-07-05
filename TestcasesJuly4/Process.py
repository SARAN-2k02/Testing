import json
import requests
import logging
import time


class ApiAutomationProcess:
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


    def infra_live_process(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name=process"
        header = {
            "Authorization": f"bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        print(f" API LOADED TIME : {response.elapsed.total_seconds()} seconds")

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

        data = response.json()
        format_data = json.dumps(data, indent=4)
        print(f" INFRA LIVE PROCESS RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --INFRA LIVE PROCESS API END-- ******************************")

    def process_graph(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/process-graph?host_name=testing&from=1720173540995&to=1720174440995&service_tag=-"
        header = {
            "Authorization": f"bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        time.sleep(5)

        print(f" PROCESS GRAPH API LOADED TIME : {response.elapsed.total_seconds()} seconds")

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

        # print(response,"pavithra")
        time.sleep(10)
        data = response.json()
        print("SARAN",data['message'])
        format_data = json.dumps(data, indent=4)
        print(f" PROCESS GRAPH API RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** -- PROCESS GRAPH API END-- ******************************")


Process_api = ApiAutomationProcess()
Process_api.login_valid_user()
Process_api.infra_live_process()
Process_api.process_graph()