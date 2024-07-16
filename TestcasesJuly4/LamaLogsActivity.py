import json
import requests
import logging
import Config


class ApiAutomationLama:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def logs_activity(self):
        url = "https://api.zoomview.ai/saas-lama/api/coc/report/datalog/activity_log/UAT?user_id=6653559ce24c5c262661c11c&from=1720238377786&to=1720241977786&datacenter="
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f" ACTIVITY API LOADED TIME : {time} seconds")

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

        format_data = response.json()['message']
        data = json.dumps(format_data, indent=4)

        if data == "":
            print(data)
        else:
            print(f"There is no data in this API")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --LOGS ACTIVITY API END-- ******************************")


Activity_api = ApiAutomationLama()
Activity_api.logs_activity()
