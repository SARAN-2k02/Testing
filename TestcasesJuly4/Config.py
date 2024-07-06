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




