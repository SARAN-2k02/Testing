import json
import requests
import logging
import Config


class ApiAutomation_Tuning:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def Log_attribute(self):
        url = "https://lab-api-zoomview.zybisys.com/saas-zoomview/api/v1/logmonitoring/log_attribute"
        header = {
            "Authorization": f"bearer {Config.lab_token}"
        }

        response = requests.get(url, headers=header)
        print(f"LOG ATTRIBUTE  API LOAD TIME : {response.elapsed.total_seconds()} seconds")

        sts_code = response.status_code
        if response.status_code == 201:
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
        print(f" LOG ATTRIBUTE API RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** -LOG ATTRIBUTE API END-- ******************************")

tuning_api = ApiAutomation_Tuning()
tuning_api.Log_attribute()