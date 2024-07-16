import json
import requests
import logging
import Config


class ApiAutomationRoles:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def roles(self):
        url = "https://api.zoomview.ai/saas-auth/api/v1/role"
        if not Config.token:
            print(f"TOKEN IS NOT PRESENT")

        header = {
            "Authorization": f"bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"ROLES API  LOAD TIME : {time} seconds")
        print(response.json())

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

        data = response.json()['message']
        format_data = json.dumps(data, indent=4)
        if format_data:
            print(f" ROLES API RESPONSE DATA :  {format_data} ")
            self.logger = logging.getLogger()
            self.logger.info("********************** --ROLES API END-- ******************************")
        else:
            print("There is no DATA is present in API")


    def group(self):
            url = "https://api.zoomview.ai/saas-auth/api/v1/role/group"
            if not Config.token:
                print(f"TOKEN IS NOT PRESENT")

            header = {
                "Authorization": f"bearer {Config.token}"
            }
            response = requests.get(url, headers=header)
            seconds = response.elapsed.total_seconds()
            time = str(seconds)[0:4]
            print(f"GROUP API  LOAD TIME : {time} seconds")
            print(response.json())

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

            data = response.json()['message']
            format_data = json.dumps(data, indent=4)
            print(f" GROUP API RESPONSE DATA :  {format_data} ")

            self.logger = logging.getLogger()
            self.logger.info("********************** --GROUP API END-- ******************************")

    def sub_cust(self):
        url = "https://api.zoomview.ai/saas-auth/api/v1/sub-cust"
        if not Config.token:
            print(f"TOKEN IS NOT PRESENT")

        header = {
            "Authorization": f"bearer {Config.token}"
        }
        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"SUB CUSTOMER API  LOAD TIME : {time} seconds")
        print(response.json())

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

        data = response.json()['message']
        format_data = json.dumps(data, indent=4)
        print(f" SUB CUSTOMER API RESPONSE DATA :  {format_data} ")

        print("    ")
        self.logger = logging.getLogger()
        self.logger.info("********************** --SUB CUSTOMER API END-- ******************************")

    def create_role(self):
        url = "https://api.zoomview.ai/saas-auth/api/v1/role"
        headers = {
            "Authorization": f"bearer {Config.token}"
        }
        role_data = {
            "role_name": "new test role",
            "color_name": "#1677FF",
            "role_action": [{"group_name": "profile", "group_action": ["view"]}]
        }
        response = requests.post(url, headers=headers, json=role_data)
        print("POST Response Status Code is :", response.status_code)
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

        if response.status_code == 201:
            data = response.json()['message']
            format_data = json.dumps(data, indent=4)
            print(f"POST Response CREATED DATA  :{format_data}")
            print(f"Role {role_data['role_name']} has been created ")
            self.logger = logging.getLogger()
            self.logger.info("********************** --CREATE ROLE API END-- ******************************")

        else:
            print("POST Request Failed")

    def update_role(self):
        put_url = "https://api.zoomview.ai/saas-auth/api/v1/role"
        headers = {
            "Authorization": f"bearer {Config.token}"
        }
        role_data = {
            "role_name": "new test role",
            "role_action": [
                {
                    "group_name": "roles",
                    "group_action": [
                        "view"
                    ]
                }
            ],
            "color_name": "#1677FF"
        }

        response = requests.put(put_url, headers=headers, json=role_data)
        print("PUT Response Status Code:", response.status_code)
        if response.status_code == 200:
            print("PUT Response JSON:", response.json())
            print(f"status code is {response.status_code}")
            print(f"Role has been updated ")
        else:
            print("PUT Request Failed")
        if response.headers['Content-Type'] == 'application/json; charset=utf-8':
            print(response.headers['Content-type'])
            print(f"Valid Header is present")
        else:
            print(f" Invalid Header : {response.headers['Content-Type']} is present")

        self.logger = logging.getLogger()
        self.logger.info("********************** --UPDATE ROLE  API END-- ******************************")

    def delete_role(self):
        url = "https://api.zoomview.ai/saas-auth/api/v1/role"
        headers = {
            "Authorization": f"bearer {Config.token}"
        }
        role = "New test role"
        delete_url = f"{url}/{role}"

        response = requests.delete(delete_url, headers=headers)

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


        print("DELETE Response Status Code:", response.status_code)
        if response.status_code == 200:
            print("DELETE Request Successful")
        else:
            print("DELETE Request Failed")

        self.logger = logging.getLogger()
        self.logger.info("********************** --DELETE ROLE API END-- ******************************")


roles_api = ApiAutomationRoles()
roles_api.roles()
roles_api.group()
roles_api.sub_cust()
roles_api.create_role()
roles_api.update_role()
roles_api.delete_role()




