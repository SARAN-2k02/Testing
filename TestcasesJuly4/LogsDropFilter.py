import json
import requests
import logging
import Config


class ApiAutomation_Drop_filter:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def Log_drop(self):
        url = "https://lab-api-zoomview.zybisys.com/saas-zoomview/api/v1/logmonitoring/log_drop"
        header = {
            "Authorization": f"bearer {Config.lab_token}"
        }

        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"LOG DROP API LOAD TIME : {time} seconds")

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
        print(f"LOG DROP API RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** -LOG DROP API END-- ******************************")


log_drop_api = ApiAutomation_Drop_filter()
log_drop_api.Log_drop()
