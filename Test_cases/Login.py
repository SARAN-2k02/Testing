import json
import requests


class APIAutomation:
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
        format_data = json.dumps(data, indent=4)
        print(format_data)
        print(data["message"])
        assert data["message"]["first_name"] == "Anshul"
        assert data["message"]["last_name"] == "Reejonia"
        print("Login successful. Token:", self.token)

    def get_status(self):
        url = "https://api.zoomview.ai/saas-zoomview/lama/licence_status"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        data = response.json()
        format_data = json.dumps(data, indent=4)
        print(format_data)
        print(data, "saran")
        assert "message" in data

    def get_host_details(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/host"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        print(response.json())

    def get_host_service(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/overall-host-service"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        print(response.json())

        data = response.json()["message"]
        print(data[2])
        # print(data["service_count"])
        for item in data:
            service_count = item['service_count']
            print(f"service count : {service_count}")
        print("GET HOST SERVICES END")

    def lama_overview_api(self):
        url = "https://api.zoomview.ai/saas-lama/api/coc/report/overview/details/UAT?user_id=6653559ce24c5c262661c11c&datacenter="
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        print(response.json())

        print("LAMA OVERVIEW API END")

    def lama_member_details(self):
        url = "https://api.zoomview.ai/saas-lama/api/coc/report/customer/details/UAT?datacenter="
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        print(response.json())




        print("LAMA MEMBER API END")


api_automation = APIAutomation()
api_automation.login_valid_user()
# api_automation.get_status()
# api_automation.get_host_details()
# api_automation.get_host_service()
# api_automation.lama_overview_api()
api_automation.lama_member_details()
