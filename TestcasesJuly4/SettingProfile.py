import json
import requests
import logging
import Config


class ApiAutomationProfile:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def profile(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/download/agents"
        if not Config.token:
            print(f"TOKEN IS NOT PRESENT")

        header = {
            "Authorization": f"bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        print(f"PROFILE API  LOAD TIME : {response.elapsed.total_seconds()} seconds")

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

        data = response.json()['message']
        format_data = json.dumps(data, indent=4)
        print(f" PROFILE API RESPONSE DATA :  {format_data} ")

        self.logger = logging.getLogger()
        self.logger.info("********************** --PROFILE API END-- ******************************")


profile_api = ApiAutomationProfile()
profile_api.profile()

