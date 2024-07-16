import json
import requests
import logging


class ApiAutomationMetrics:
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

    def metrics_data(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/metrixdata?host_name=testing"
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)

        sts_code = response.status_code
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f" METRICS DATA API LOADED TIME : {time} seconds")
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
        print(f"  METRICS DATA API RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --METRICS DATA API END-- ******************************")


Metrics_api = ApiAutomationMetrics()
Metrics_api.login_valid_user()
Metrics_api.metrics_data()