import json
import requests
import logging
import Config


class ApiAutomationDocument:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def Plugin_list_windows(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/download/pluginlist?os=windows"
        if not Config.token:
            print(f"TOKEN IS NOT PRESENT")

        header = {
            "Authorization": f"bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f" PLUGIN LIST WINDOWS API LOADED TIME : {time} seconds")

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
        print(f" PLUGIN LIST WINDOWS API RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --PLUGIN LIST WINDOWS API END-- ******************************")

    def Plugin_list_linux(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/download/pluginlist?os=linux"
        header = {
            "Authorization": f"bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"PLUGIN LIST LINUX API LOADED TIME :{time} seconds ")

        sts_code = response.status_code == 201
        if sts_code:
            print(f"Status Code {sts_code} is present")
        else:
            print(f"Invalid status code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        data = response.json()
        format_data = json.dumps(data, indent=4)
        if format_data:
            print(f" PLUGIN LIST LINUX API RESPONSE DATA :  {format_data} ")
            self.logger = logging.getLogger()
            self.logger.info("********************** --PLUGIN LIST LINUX API END-- ******************************")
        else:
            print(f"there is not data in API")


docs_api = ApiAutomationDocument()
docs_api.Plugin_list_windows()
docs_api.Plugin_list_linux()