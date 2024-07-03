import json
import requests


class ApiAutomationInfra:
    def __init__(self):
        self.token = None

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
        print("token", self.token)

    def host_details(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/host"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        Api_load = response.elapsed.total_seconds()
        # ss = str(Api_load)[:4]
        # print(ss)
        print(f"API LOADED TIME : ", {response.elapsed.total_seconds()})

        host_data = response.json()
        # print(host_data)
        formated_data = json.dumps(host_data, indent=4)
        print(formated_data)
        host_message = host_data["message"]

        for item in host_message:
            print("Host id : ", item['_id'])
            print("Customer Id : ", item['customer_id'])

        print("-----------------------------------------------------------------------")
        print("---------------------HOST DETAILS END----------------------------------")
        print("-----------------------------------------------------------------------")

    def overall_host(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/overall-host-service"
        header = {
            "Authorization":f"Bearer {self.token}"
        }

        response = requests.get(url, headers=header)
        assert response.status_code == 200
        # print(response.json())
        overall_data = response.json()["message"]
        print(overall_data)

        for status in overall_data:
            print(status)



infra_api = ApiAutomationInfra()
infra_api.login_valid_user()
infra_api.host_details()
infra_api.overall_host()
