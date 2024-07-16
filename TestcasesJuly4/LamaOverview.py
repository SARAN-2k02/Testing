import json
import requests
import logging
import Config


class ApiAutomationLama:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def Customer_details(self):
        url = "https://api.zoomview.ai/saas-lama/api/coc/report/customer/details/UAT?datacenter="
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        # print(response.json())
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f" API LOADED TIME : {time} seconds")

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
        print(f" LAMA CUSTOMER DETAILS API  RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --CUSTOMER DETAILS API END-- ******************************")

    def Datacenter_details(self):
        url = "https://api.zoomview.ai/saas-lama/api/coc/report/overview/details/UAT?user_id=6653559ce24c5c262661c11c&datacenter="
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        # print(response.json())
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f" Datacenter Details API LOADED TIME : {time} seconds")

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
        print(f" DATACENTER DETAILS API  RESPONSE DATA :  {format_data} ")

        self.logger = logging.getLogger()
        self.logger.info(f"********************** --{"DATACENTER DETAILS"} API END-- ******************************")

    def Exchange_details(self):
        url = "https://api.zoomview.ai/saas-lama/api/coc/report/overview/details/UAT?user_id=6653559ce24c5c262661c11c&datacenter="
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        # print(response.json())
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f" Exchange Details API LOADED TIME : {time} seconds")

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
        print(f" DATACENTER DETAILS API  RESPONSE DATA :  {format_data} ")

        self.logger = logging.getLogger()
        self.logger.info(f"********************** --{"EXCHANGE DETAILS"} API END-- ******************************")


Overview_api = ApiAutomationLama()
Overview_api.Customer_details()
Overview_api.Datacenter_details()
Overview_api.Exchange_details()


