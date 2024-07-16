import json
import requests
import logging
import Config


class ApiAutomationSignUp:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def Signup(self):
        url = "https://api.zoomview.ai/saas-auth/api/v1/auth/signup"
        body = {
            "first_name": "aron",
            "last_name": "raj",
            "designation": "Doctor",
            "email": "hjraj@mail.com",
            "phone": "9980389567",
            "password": "Demo@1234",
            "company_name": ""
        }
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.post(url, json=body)

        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f" SIGNUP API  LOAD TIME : {time} seconds")

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
        print(f" SIGNUP API RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --SIGNUP API END-- ******************************")


Signup_Api = ApiAutomationSignUp()
Signup_Api.Signup()


