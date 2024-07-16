import json
import requests
import logging
import Config


class ApiAutomationSummary:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


    def infra_live_state_cpu(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name=cpu"
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        sts_code = response.status_code

        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"INFRA LIVE STATE CPU API LOADED TIME : {time} seconds")

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


        self.logger = logging.getLogger()
        self.logger.info("********************** --INFRA LIVE STATE CPU API END-- ******************************")

    def infra_ram_graph(self):
        url = ("https://api.zoomview.ai/saas-zoomview/api/v1/infra/ram-graph?host_name=fero007&from=1721111580227&to=1721112480227&service_tag=-")
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        # assert response.status_code == 200

        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"INFRA RAM GRAPH API LOADED TIME : {time} seconds")

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

    def cpu_graph(self):
        print("cpu graph api start")
        url = ("https://api.zoomview.ai/saas-zoomview/api/v1/infra/cpu-graph?host_name=fero007&from=1721111470894&to=1721112370895&service_tag=")

        header = {
            "Authorization": f"bearer {Config.token}"
        }

        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"CPU GRAPH API LOADED TIME : {time} seconds")

        # print(response)
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

        cpu_data = response.json()["message"]
        format_cpu_data = json.dumps(cpu_data, indent=4)
        print(f"CPU DATA : {format_cpu_data}")

        for data in cpu_data:
            service_name = data["service_name"]
            if service_name:
                print(f"Service name {service_name} is present")
            else:
                print(f"Service name is not present ")

            service_tag = data.get("service_tag")
            if service_tag:
                print(f"service tag {service_tag} is present")

            version = data.get('__v')
            if version == 0:
                print(f"version {version} present")

            break

        print("--------")
        self.logger = logging.getLogger()
        self.logger.info("********************** --CPU GRAPH API END-- ******************************")

    def list_host(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate/list?host_name=testing&service_name=interface"
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        assert response.status_code == 200
        sts_code = response.status_code

        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"LIST HOST API LOADED TIME : {time} seconds")
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

        list_host_data = response.json()["message"]
        format_host = json.dumps(list_host_data, indent=4)
        print(f"list host data : {format_host}")

        # checking lan-flag,service tag , version is present in API or not

        for data in list_host_data:
            service_tag = data.get("service_tag")
            if service_tag:
                print(f"service tag : {service_tag} is present ")

            lan_flag = data.get('lan_flag')
            if lan_flag == True:
                print(f"lan flag value is True")
            else:
                print(f"lan-flag value is False")

        print("----")
        self.logger = logging.getLogger()
        self.logger.info("********************** --LIST HOST API END-- ******************************")

    def testing_server(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/host_service_status/testing"
        header = {
            "Authorization": f"Bearer {Config.token}"
        }

        response = requests.get(url, headers=header)
        sts_code = response.status_code

        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"TESTING SERVER API LOADED TIME : {time} seconds")
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

        testing_data = response.json()['message']
        print(f" Server Api Data :  {json.dumps(testing_data, indent=4)}")
        for data in testing_data:
            status = data['_id']['status']
            service_count = data['service_count']
            print(f"Services for INSTANCE IS {service_count} and status is {status} ")

        self.logger = logging.getLogger()
        self.logger.info("********************** --TESTING SERVER API END-- ******************************")

    def infra_livestate_ram(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name=ram"
        header = {
            "Authorization": f"Bearer {Config.token}"
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
        print(f" INFRA LIVE RAM APIP DATA :  {format_data} ")

        self.logger = logging.getLogger()
        self.logger.info("************************************-- INFRA LIVE RAM API END- --**************************")

    def infra_live_disk(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name=disk"
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)

        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"INFRA LIVE DISK API LOADED TIME : {time} seconds")

        disk_data = response.json()['message']
        for data in disk_data:
            id = data["_id"]
            customer_id = data['customer_id']
            service_name = data['service_name']

            print(f"Customer Id is {customer_id} is present")
            print(f"Id is {id} is present ")

            if service_name:
                print(f"Service name is present")
            else:
                print("service name not present")

            break

        format_disk_data = json.dumps(disk_data, indent=4)
        print(f" INFRA LIVE DISK DATA : {format_disk_data}")
        self.logger = logging.getLogger()
        self.logger.info("************************************-- INFRA LIVE DISK API END- --**************************")

    def infra_live_process(self):
        url = ("https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name"
               "=process")
        header = {
            "Authorization": f"Bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        # assert response.status_code == 200
        sts_code = response.status_code

        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"INFRA LIVE PROCESS API LOADED TIME : {time} seconds")
        if response.status_code == 200:
            print(f"Status Code is 200")
        else:
            print(f"invalid Status Code {sts_code} is present")

        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        process_data = response.json()['message']


        for data in process_data:
            id = data["_id"]
            customer_id = data['customer_id']
            service_name = data['service_name']
            service_tag = data['service_tag']

            print(f"Customer Id is {customer_id} present")
            print(f"Id is {id} present")
            print(f"Service tag is {service_tag} is present")

            if service_name:
                print(f"Service name is {service_name} is present ")
            else:
                print("service name not present")
            break

        self.logger = logging.getLogger()
        process_data_format = json.dumps(process_data, indent=4)
        print(f"Infra live process api data : {process_data_format}")
        self.logger.info("************************************-- INFRA LIVE PROCESS API END- --**************************")

    def interface_graph(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/interface-graph?host_name=testing&from=1720154231033&to=1720155131034&service_tag=ens160"

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
        # print(f"Host name : {data['host_name']} ")
        interface_graph_data = json.dumps(data, indent=4)
        print(f"interface Api data : {interface_graph_data}")
        self.logger = logging.getLogger()
        self.logger.info("************************************-- INTERFACE GRAPH API END- --**************************")


summary_api = ApiAutomationSummary()
summary_api.infra_live_state_cpu()
summary_api.infra_ram_graph()
summary_api.cpu_graph()
summary_api.list_host()
summary_api.testing_server()
summary_api.infra_livestate_ram()
summary_api.infra_live_disk()
summary_api.infra_live_process()
summary_api.interface_graph()

