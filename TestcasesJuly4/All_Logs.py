import json
import requests
import logging
import Config


class ApiAutomation_All_Logs:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def Opensearch(self):
        # print(self.token, "TOKEN")
        url = "https://lab-api-zoomview.zybisys.com/saas-zoomview/api/v1/fluent//log_parse_filters/opensearch?apiversion=1&limit=25&from=1720440300273"
        header = {
            "Authorization": f"bearer {Config.lab_token}"
        }

        response = requests.post(url, headers=header)
        print(f"ALL LOGS API LOAD TIME : {response.elapsed.total_seconds()} seconds")

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
        print(f" ALL LOGS RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** -OPENSEARCH API END-- ******************************")

    def graph_builder(self):
        url = "https://lab-api-zoomview.zybisys.com/saas-zoomview/api/v1/opensearch/opensearch/graph_builder?from=1720440194971&to=1720441094971&group_by=by_minute"

        header = {
            "Authorization": f"bearer {Config.lab_token}"
        }

        response = requests.get(url, headers=header)
        print(f"GRAPH BUILDER  API LOAD TIME : {response.elapsed.total_seconds()} seconds")

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
        print(f" GRAPH BUILDER API RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** -GRAPH BUILDER API END-- ******************************")

all_logs_api = ApiAutomation_All_Logs()
all_logs_api.Opensearch()
all_logs_api.graph_builder()