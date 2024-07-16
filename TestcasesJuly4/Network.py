import json
import requests
import logging
import Config


class ApiAutomationNetwork:
    def __init__(self):
        self.logger = None
        self.token = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



    def interface_graph(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/interface-graph?host_name=testing&from=1720172640710&to=1720173540710&service_tag=-"

        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        sts_code = response.status_code

        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"INTERFACE GRAPH API LOADED TIME : {time} seconds")

        if response.status_code == 200:
            print(f"Status Code is 200")
        else:
            print(f"invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        data = response.json()['message']
        interface_graph_data = json.dumps(data, indent=4)
        print(f"Interface Api data : {interface_graph_data}")
        self.logger = logging.getLogger()
        self.logger.info("************************************-- INTERFACE GRAPH API END- --**************************")

    def infra_live_interface(self):
        url = 'https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name=interface'
        header = {
            "Authorization": f"bearer {Config.token}"
        }

        response = requests.get(url, headers=header)

        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f" INTERFACE API LOADED TIME : {time} seconds")
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
        print(f" LOGIN RESPONSE DATA :  {format_data} ")

        self.logger = logging.getLogger()
        self.logger.info("************************************--INFRA LIVE INTERFACE API END- --**************************")


network_api = ApiAutomationNetwork()
network_api.interface_graph()
network_api.infra_live_interface()
