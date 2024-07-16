import json
import requests
import logging


class ApiAutomationAlert:
    def __init__(self):
        self.logger = None
        self.token = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def login_valid_user(self):
        url = "https://api.zoomview.ai/saas-auth/api/v1/auth/login"
        body = {
            "email": "anshul.reejonia@zybisys.com",
            "password": "Demo@1234"
        }
        response = requests.post(url, json=body)
        assert response.status_code == 200
        data = response.json()
        self.token = data["message"]["token"]

    def testing_server(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/service_alert_dashboard/testing"
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f" TESTING SERVER API LOADED TIME : {time} seconds")

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
        print(f" TESTING SERVER API RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --TESTING SERVER API END-- ******************************")


Alert_api = ApiAutomationAlert()
Alert_api.login_valid_user()
Alert_api.testing_server()