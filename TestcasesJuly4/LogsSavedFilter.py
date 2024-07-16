import json
import requests
import logging
import Config


class ApiAutomation_Saved_Filter:
    def __init__(self):
        self.logger = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def log_views(self):
        url = "https://lab-api-zoomview.zybisys.com/saas-zoomview/api/v1/logmonitoring/log_views"
        header = {
            "Authorization": f"bearer {Config.lab_token}"
        }

        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"LOG view API LOAD TIME : {time} seconds")

        sts_code = response.status_code
        if response.status_code == 201:
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
        print(f"LOG VIEW API RESPONSE DATA :  {format_data} ")
        self.logger = logging.getLogger()
        self.logger.info("********************** -LOG view API END-- ******************************")

    def graph_builder(self):
        url = "https://lab-api-zoomview.zybisys.com/saas-zoomview/api/v1/opensearch/opensearch/graph_builder?from=1720441256629&to=1720442156629&group_by=by_minute"

        header = {
            "Authorization": f"bearer {Config.lab_token}"
        }

        response = requests.get(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"GRAPH BUILDER  API LOAD TIME : {time} seconds")

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

    def Opensearch(self):
        # print(self.token, "TOKEN")
        url = "https://lab-api-zoomview.zybisys.com/saas-zoomview/api/v1/fluent//log_parse_filters/opensearch?apiversion=1&limit=25&from=1720440300273"
        header = {
            "Authorization": f"bearer {Config.lab_token}"
        }

        response = requests.post(url, headers=header)
        seconds = response.elapsed.total_seconds()
        time = str(seconds)[0:4]
        print(f"OPEN SEARCH API LOAD TIME : {time} seconds")

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
        print(f" OPEN SEARCH API RESPONSE DATA :  {format_data} ")

        print("   ")
        self.logger = logging.getLogger()
        self.logger.info("********************** -OPENSEARCH API END-- ******************************")


log_drop_api = ApiAutomation_Saved_Filter()
log_drop_api.log_views()
log_drop_api.graph_builder()
log_drop_api.Opensearch()



