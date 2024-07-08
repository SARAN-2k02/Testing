import requests
import json


url = "https://api.zoomview.ai/saas-auth/api/v1/auth/login"
body = {
    "email": "anshul.reejonia@zybisys.com",
    "password": "Demo@1234"
}
response = requests.post(url, json=body)
assert response.status_code == 200
data = response.json()
token = data["message"]["token"]
# token = ""
# print(token)



lab_url = "https://lab-api-zoomview.zybisys.com/saas-auth/api/v1/auth/login"
lab_body = {
        "email":"anshul.reejonia@zybisys.com",
        "password":"Anshul@321"
    }
lab_response = requests.post(lab_url, json=lab_body)

lab_data = lab_response.json()['message']
lab_token = lab_data['token']
# print(lab_token)


