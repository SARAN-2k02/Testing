import json
import requests
import logging
import config


class ApiAutomationInfo:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def host_info(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/hostinfo?host_name=testing"
        header = {
            "Authorization": f"Bearer {config.token}"
        }
        response = requests.get(url, headers=header)
        print(f" HOST INFO API LOADED TIME : {response.elapsed.total_seconds()} seconds")
        # print(response.json())

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
        print(f" HOST INFO RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --HOST INFO API END-- ******************************")

    def software_info(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/software-inventory?host_name=testing"
        header = {
            "Authorization": f"Bearer {config.token}"
        }
        response = requests.get(url, headers=header)
        print(f" HOST INFO API LOADED TIME : {response.elapsed.total_seconds()} seconds")
        # print(response.json())

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
        print(f" SOFTWARE INFO RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --SOFTWARE INFO API END-- ******************************")


Info_api = ApiAutomationInfo()
Info_api.host_info()
Info_api.software_info()



