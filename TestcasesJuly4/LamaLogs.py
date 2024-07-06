import json
import requests
import logging
import Config


class ApiAutomationLama:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def Uat_logs_one(self):
        url = "https://api.zoomview.ai/saas-lama/api/coc/report/customer/details/UAT?datacenter="
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        # print(response.json())
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
        print(f"  LAMA LOGS ONE API  RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --UAT LOGS ONE API END-- ******************************")

    def Uat_log_two(self):
        url = "https://api.zoomview.ai/saas-lama/api/coc/report/datalog/exchange_log/UAT?user_id=6653559ce24c5c262661c11c&from=1720240419194&to=1720241319194&log=system&exchange=all&datacenter="
        header = {
            "Authorization": f"Bearer {config.token}"
        }
        response = requests.get(url, headers=header)
        # print(response.json())
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
        print(f" LAMA LOGS TWO API  RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --UAT LOGS TWO API END-- ******************************")


Logs_api = ApiAutomationLama()
Logs_api.Uat_logs_one()
Logs_api.Uat_log_two()