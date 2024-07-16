import json
import requests
import logging
import Config


class ApiAutomationForgetPass:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def Forgot_Password(self):
        email = "saran2002raj@gmail.com"
        url = f"https://api.zoomview.ai/saas-auth/api/v1/auth/forgot-password/{email}"
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"FORGOT PASSWORD API  LOAD TIME : {time} seconds")

        sts_code = response.status_code
        if response.status_code == 200:
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
        print(f" FORGOT PASSWORD RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --FORGOT PASSWORD API END-- ******************************")


forgot_api = ApiAutomationForgetPass()
forgot_api.Forgot_Password()