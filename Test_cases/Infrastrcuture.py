import json
import requests



class Api_Automation_Infra:
    def __init__(self):
        self.token = None

    def host_details(self):
        url = "https://api.zoomview.ai/saas-zoomview/api/v1/infra/host"
