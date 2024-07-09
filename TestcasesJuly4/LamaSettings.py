import json
import requests
import logging
import Config


class ApiAutomationLama:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def settings_host(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/host"
        if not Config.token:
            print(f"TOKEN IS NOT PRESENT")

        header = {
            "Authorization": f"bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        print(f" LAMA SETTING HOST API  LOAD TIME : {response.elapsed.total_seconds()} seconds")

        sts_code = response.status_code
        if response.status_code == 200:
            print(f"Status Code is 200")
        else:
            print(f"Invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"Valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        data = response.json()
        format_data = json.dumps(data, indent=4)
        print(f" HOST API RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --LAMA SETTING API END-- ******************************")

    def settings_uat(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/host"
        if not Config.token:
            print(f"TOKEN IS NOT PRESENT")
        header = {
            "Authorization": f"bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        print(f"LAMA SETTING API  LOAD TIME : {response.elapsed.total_seconds()} seconds")

        sts_code = response.status_code
        if response.status_code == 200:
            print(f"Status Code is 200")
        else:
            print(f"Invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"Valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        data = response.json()
        format_data = json.dumps(data, indent=4)
        print(f" LAMA SETTING UAT RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --LAMA SETTING UAT API END-- ******************************")


Setting_api = ApiAutomationLama()
Setting_api.settings_host()
Setting_api.settings_uat()

