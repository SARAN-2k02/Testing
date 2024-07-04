import json
import requests
import logging


class APIAutomationDashboard:
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
        # assert response.status_code == 200
        sts_code = response.status_code
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
        self.token = data["message"]["token"]
        self.logger = logging.getLogger()
        self.logger.info("********************** --LOGIN API END-- ******************************")

    def get_status(self):
        url = "https://api.zoomview.ai/saas-zoomview/lama/licence_status"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        sts_code = response.status_code
        if response.status_code == 200:
            print(f"Status Code is 200")
        else:
            print(f"invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"valid Header is present")
        else:
            print(f"Invalid Header {response.headers['Content-type']} is present ")

        data = response.json()
        format_data = json.dumps(data, indent=4)
        print(format_data)
        self.logger = logging.getLogger()
        self.logger.info("********************** --GET HOST STATUS API END-- ******************************")



    def get_host_details(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/host"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        print(response.json())


        sts_code = response.status_code
        if response.status_code == 200:
            print(f"Status Code is 200")
        else:
            print(f"invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"valid Header is present")
        else:
            print(f"Invalid Header {response.headers['Content-type']} is present ")

        data = response.json()
        format_data = json.dumps(data, indent=4)
        print(format_data)

        self.logger = logging.getLogger()
        # print()
        self.logger.info("********************** --GET HOST DETAILS API END-- ******************************")

    def get_host_service(self):

        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/overall-host-service"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        print(response.json())

        data = response.json()["message"]
        print(" DATA TWO",data[2])
        for item in data:
            service_count = item['service_count']
            status = item['status']
            print(f"service count : {service_count} is {status} status ")
            # print(f"status count : {status}")
        # print("GET HOST SERVICES END")

        format_data = json.dumps(data, indent=4)
        # print(format_data)
        print(f" Get host service API data :  {format_data} ")
        self.logger = logging.getLogger()

        self.logger.info("********************** --GET HOST SERVICE API END-- ******************************")

    def lama_overview_api(self):
        url = "https://api.zoomview.ai/saas-lama/api/coc/report/overview/details/UAT?user_id=6653559ce24c5c262661c11c&datacenter="
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        # print(response.json())
        sts_code = response.status_code
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

        data = response.json()['data']
        format_data = json.dumps(data, indent=4)
        print(f" Lama overview API data :  {format_data} ")

        self.logger = logging.getLogger()
        self.logger.info("********************** --LAMA OVERVIEW API END-- ******************************")
        # print("LAMA OVERVIEW API END")

    def lama_member_details(self):
        url = "https://api.zoomview.ai/saas-lama/api/coc/report/customer/details/UAT?datacenter="
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)

        sts_code = response.status_code
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
        format_data = json.dumps(data, indent=4)
        print(f" LAMA MEMBER API DATA :  {format_data} ")

        self.logger = logging.getLogger()
        self.logger.info("********************** --LAMA MEMBER API END-- ******************************")
        # print("LAMA MEMBER API END")


api_automation = APIAutomationDashboard()
api_automation.login_valid_user()
api_automation.get_status()
api_automation.get_host_details()
api_automation.get_host_service()
api_automation.lama_overview_api()
api_automation.lama_member_details()


