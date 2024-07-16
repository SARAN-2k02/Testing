import requests
import logging
import json


class ApiAutomationSystem:
    def __init__(self):
        self.token = None
        self.logger = None
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
        # print(self.token)
        # print("HEY SARAN")

    def cpu_graph(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/cpu-graph?host_name=testing&from=1720162200296&to=1720163100296&service_tag=-"

        header = {
            "Authorization": f"bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        # print(response)
        sts_code = response.status_code

        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"CPU GRAPH API LOADED TIME :  {time} seconds")

        if response.status_code == 200:
            print(f"Status Code is 200")
        else:
            print(f"invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        cpu_data = response.json()["message"]
        format_cpu_data = json.dumps(cpu_data, indent=4)
        print(f"CPU DATA : {format_cpu_data}")

        for data in cpu_data:
            service_tag = data.get("service_tag")
            if service_tag:
                print(f"service tag {service_tag} is present")

            version = data.get('__v')
            if version == 0:
                print(f"version {version} present")

            break

        print("--------")
        self.logger = logging.getLogger()
        self.logger.info(f"********************** --CPU GRAPH API END-- ******************************")

    def System_ram_graph(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/ram-graph?host_name=testing&from=1720162200296&to=1720163100296&service_tag=-"
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        # assert response.status_code == 200

        sts_code = response.status_code
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"SYSTEM RAM GRAPH API LOADED TIME :  {time} seconds")
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

        graph_data = response.json()["message"]
        format_data = json.dumps(graph_data, indent=4)
        print("INFRA RAM GRAPH DATA :", format_data)

        # comparing API that service name and id is present or not

        for data in graph_data:
            id = data.get("_id")
            if id:
                print(f"Id {id} is present in API")

            # verifying service is 0 or not
            version = data.get('__v')
            if version == 0:
                print(f"The Version {version} is present ")
            else:
                print("version is not present")

        self.logger = logging.getLogger()
        self.logger.info("********************** --RAM GRAPH END-- ******************************")

    def infra_live_state_cpu(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name=cpu"
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        sts_code = response.status_code
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"INFRA LIVE STATE CPU API LOADED TIME :  {time} seconds")

        if response.status_code == 200:
            print(f"Status Code is 200")
        else:
            print(f"invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        live_data = response.json()["message"]
        for data in live_data:
            if "host_name" in data:
                print(f"HOSTNAME {data["host_name"]} is present")

            service_data = data.get("service_data")
            if service_data:
                format_data = json.dumps(service_data, indent=4)
                print(f"Service data is {format_data} present ")

            print("-----")
        self.logger = logging.getLogger()
        self.logger.info("********************** --INFRA LIVE STATE CPU API END-- ******************************")

    def infra_live_ram(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name=ram"
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"INFRA LIVE RAM API LOADED TIME : {time} seconds")
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

        data = response.json()
        ram_data = response.json()['message']
        format_data = json.dumps(ram_data, indent=4)
        print(f" INFRA LIVE RAM API DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("************************************-- INFRA LIVE RAM API END- --**************************")


system_api = ApiAutomationSystem()
system_api.login_valid_user()
system_api.cpu_graph()
system_api.System_ram_graph()
system_api.infra_live_state_cpu()
system_api.infra_live_ram()