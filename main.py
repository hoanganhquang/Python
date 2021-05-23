import requests
from datetime import datetime

app_ID = ""
app_Key = ""

input_ = input("Tell me which exercises you did: ")

parameters = {
    "query": input_,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 170,
    "age": 21
}

headers = {
    "x-app-id": app_ID,
    "x-app-key": app_Key,
}

url = ""

response = requests.post(url=url, json=parameters, headers=headers)
data = response.json()

url_sheet = ""
date = datetime.now()
day = date.strftime("%d/%m/%Y")
time = date.strftime("%X")

headers_sheet = {
    ""
}

for exercise in data["exercises"]:
    parameters_sheet = {
        "workout": {
            "date": day,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    requests.post(url=url_sheet, json=parameters_sheet, headers=headers_sheet)
# Ran 5k and cycled for 20 minutes



