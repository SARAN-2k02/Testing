import json
import requests


class ApiAutomationSummary:
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

    def infra_live_state_cpu(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name=cpu"
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        assert response.status_code == 200
        # print(response.json())

        live_data = response.json()["message"]
        print(live_data)

        for data in live_data:

            if "host_name" in data:
                print(f"HOSTNAME {data["host_name"]} is present")

            service_data = data.get("service_data")
            if service_data:
                format = json.dumps(service_data, indent=4)
                print(f"Service data is {format} present ")

        print("-------------------------------------------------------------------------------")
        print("---------------------INFRA LIVE STATE API END----------------------------------")
        print("-------------------------------------------------------------------------------")

    def infra_ram_graph(self):
        url = ("https://api.zoomview.ai/saas-zoomview/api/v1/infra/ram-graph?host_name=testing&from=1720000428225&to"
               "=1720001328225&service_tag=-")
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        assert response.status_code == 200
        graph_data = response.json()["message"]
        print("API RESPONSE IS :", graph_data)

        # comparing API that service name and id is present or not

        for data in graph_data:
            id = data.get("_id")
            if id:
                print(f"Id {id} is present in API")

            service_name = data.get("service_name")
            if service_name:
                print(f"Service name : {service_name} is present")

            # verifying service is 0 or not
            version = data.get('__v')
            if version == 0:
                print(f"The Version {version} is present ")
            else:
                print("version is not present")


        print(""" 
       -------------------------------------------------------------------------------------------------
       -----------------------------RAM GRAPH END-------------------------------------------------------
       -------------------------------------------------------------------------------------------------
        """)

    def cpu_graph(self):
        url = ("https://api.zoomview.ai/saas-zoomview/api/v1/infra/cpu-graph?host_name=testing&from=1720000428225&to"
               "=1720001328225&service_tag=-")

        cpu = "cpu-graph"

        for cpu in url:
            print(f"cpu-graph is present in API Url - it is cpu API")

            if "cpu-graph":
                break

        header = {
            "Authorization": f"bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        # print(response)
        assert response.status_code == 200
        if response:
            print(f"Status code : {response.status_code}")
        cpu_data = response.json()["message"]
        print(cpu_data)

        for data in cpu_data:
            service_name = data["service_name"]
            if service_name:
                print(f"Service name {service_name} present")
            else:
                print(f"Service name is not present ")

            service_tag = data.get("service_tag")
            if service_tag:
                print(f"service tag {service_tag} is present")

            version = data.get('__v')
            if version == 0:
                print(f"version {version} present")

            break

        print(""" 
             -------------------------------------------------------------------------------------------------
             -----------------------------CPU GRAPH END-------------------------------------------------------
             -------------------------------------------------------------------------------------------------
              """)

    def list_host(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate/list?host_name=testing&service_name=interface"
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        assert response.status_code == 200
        print(response.json()["message"])

        list_host_data = response.json()["message"]

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

        print(""" 
                 -------------------------------------------------------------------------------------------------
                 -----------------------------LIST HOST API END-------------------------------------------------------
                 -------------------------------------------------------------------------------------------------
                  """)

    def testing_server(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/host_service_status/testing"
        header = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url, headers=header)
        assert response.status_code == 200
        # print(response.json())
        testing_data = response.json()['message']

        for data in testing_data:
            status = data['_id']['status']
            service_count = data['service_count']
            print(f"Services for INSTANCE IS {service_count} and status is {status} ")

        print(""" 
                         -------------------------------------------------------------------------------------------------
                         -----------------------------TESTING SERVER API END-------------------------------------------------------
                         -------------------------------------------------------------------------------------------------
                          """)

    def infra_live_ram(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name=ram"
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        assert response.status_code == 200
        # print(response.json())
        ram_data = response.json()['message']
        print(ram_data)

        for data in ram_data:
            id = data["_id"]
            customer_id = data['customer_id']
            service_name = data['service_name']

            print(f"Customer Id is {customer_id}")
            print(f"Id is {id}")

            if service_name:
                print(f"Service name is {service_name}")
            else:
                print("service name not present")

            service_data = data['service_data']
            # print("service data", service_data)

            for service in service_data:
                print("metrix name is ", service['metrix_name'])
                print("metrix value is ", service['metrix_value'], service['metrix_unit'])


        print(""" 
                                 -------------------------------------------------------------------------------------------------
                                 -----------------------------INFRA LIVE RAM API END-------------------------------------------------------
                                 -------------------------------------------------------------------------------------------------
                                  """)


    def infra_live_disk(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name=disk"
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        assert response.status_code == 200
        # print(response.json())
        disk_data = response.json()['message']
        print(disk_data)

        for data in disk_data:
            id = data["_id"]
            customer_id = data['customer_id']
            service_name = data['service_name']

            print(f"Customer Id is {customer_id}")
            print(f"Id is {id}")

            if service_name:
                print(f"Service name is {service_name}")
            else:
                print("service name not present")

            service_data = data['service_data']

            for service in service_data:
                print("metrix name is ", service['metrix_name'])
                print("metrix value is ", service['metrix_value'], service['metrix_unit'])

            break

        print(""" 
                                         -------------------------------------------------------------------------------------------------
                                         -----------------------------INFRA LIVE DISK API END-------------------------------------------------------
                                         -------------------------------------------------------------------------------------------------
                                          """)

    def infra_live_process(self):
        url = ("https://api.zoomview.ai/saas-zoomview/api/v1/infra/infra-livestate?host_name=testing&service_name"
               "=process")
        header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=header)
        assert response.status_code == 200
        process_data = response.json()['message']
        print(process_data)
        print("infra live process api")

        for data in process_data:
            id = data["_id"]
            customer_id = data['customer_id']
            service_name = data['service_name']
            service_tag = data['service_tag']

            print(f"Customer Id is {customer_id}")
            print(f"Id is {id}")
            print(f"Service tag is {service_tag}")

            if service_name:
                print(f"Service name is {service_name}")
            else:
                print("service name not present")

            service_data = data['service_data']

            for service in service_data:
                print("metrix name is ", service['metrix_name'])
                print("metrix value is ", service['metrix_value'], service['metrix_unit'])

            break

    print(""" 
                             -------------------------------------------------------------------------------------------------
                             -----------------------------INFRA PROCESS API END-------------------------------------------------------
                             -------------------------------------------------------------------------------------------------
                              """)


summary_api = ApiAutomationSummary()
summary_api.login_valid_user()
summary_api.infra_live_state_cpu()
summary_api.infra_ram_graph()
summary_api.cpu_graph()
summary_api.list_host()
summary_api.testing_server()
summary_api.infra_live_ram()
summary_api.infra_live_disk()
summary_api.infra_live_process()

