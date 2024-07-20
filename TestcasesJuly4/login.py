import json
import requests
import logging


class APIAutomation:
    def __init__(self):
        self.token = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        # self.logger = logging.getLogger()
        # self.logger.info("APIAutomation Initialized")

    def login_valid_user(self):
        url = "https://api.zoomview.ai/saas-auth/api/v1/auth/login"
        body = {
            "email": "anshul.reejonia@zybisys.com",
            "password": "Demo@1234"
        }
        response = requests.post(url, json=body)
        # assert response.status_code == 200
        sts_code = response.status_code
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"LOGIN API LOADED TIME : {time} seconds")
        # print(sts_code)
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
        # print()
        self.token = data["message"]["token"]
        format_data = json.dumps(data, indent=4)
        print("   ")
        print(f" LOGIN RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --LOGIN API END-- ******************************")


login_api_automation = APIAutomation()
login_api_automation.login_valid_user()







