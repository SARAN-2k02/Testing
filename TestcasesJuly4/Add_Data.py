import json
import requests
import logging
import Config


class ApiAutomationAddData:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def get_log_group(self):
        url = "https://lab-api-zoomview.zybisys.com/saas-zoomview/api/v1/logmonitoring/get_log_group"
        header = {
            "Authorization": f"bearer {Config.lab_token}"
        }

        response = requests.get(url, headers=header)
        print(f"LOG GROUP API LOAD TIME : {response.elapsed.total_seconds()} seconds")

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
        print(f" LOG GROUP API RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** -LOG GROUP API END-- ******************************")

    def check_fluentbit(self):
        url = "https://lab-api-zoomview.zybisys.com/saas-zoomview/api/v1/logmonitoring/get_log_group"
        header = {
            "Authorization": f"bearer {Config.lab_token}"
        }

        response = requests.get(url, headers=header)
        print(f"CHECK FLUENT BIT API LOAD TIME : {response.elapsed.total_seconds()} seconds")

        sts_code = response.status_code
        if response.status_code == 201:
            print(f"Status Code is 201")
        else:
            print(f"Invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"Valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        data = response.json()
        format_data = json.dumps(data, indent=4)
        print(f" CHECK FLUENT BIT API RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** -CHECK FLUENT BIT API END-- ******************************")

    def set_log(self):
        url = "https://lab-api-zoomview.zybisys.com/saas-zoomview/api/v1/logmonitoring/set_log"
        header = {
            "Authorization": f"bearer {Config.lab_token}"
        }
        body = {
            "file_path": "coc/folderr/testdeta.txt",
            "tag_name": "newPat",
            "file_type": "nginx",
            "host_name": "WIN-KDPF1GGMQHI"
        }
        response = requests.post(url, headers=header, json=body)
        print(f"SET LOG API LOAD TIME : {response.elapsed.total_seconds()} seconds")

        sts_code = response.status_code
        if response.status_code == 201:
            print(f"Status Code is 201")
        else:
            print(f"Invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"Valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        data = response.json()
        format_data = json.dumps(data, indent=4)
        print(f"SET LOG API RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** -SET LOG API END-- ******************************")


add_data_api = ApiAutomationAddData()
add_data_api.get_log_group()
add_data_api.check_fluentbit()
add_data_api.set_log()
