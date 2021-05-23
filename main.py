import requests
from datetime import datetime

app_ID = "bee59748"
app_Key = "41599ba87596214f148f272c757fd338"

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

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=url, json=parameters, headers=headers)
data = response.json()

url_sheet = "https://api.sheety.co/c116e53c4127320e7dac36feff50582f/workoutTracking/workouts"
date = datetime.now()
day = date.strftime("%d/%m/%Y")
time = date.strftime("%X")

headers_sheet = {
    "Authorization": "Basic dGFiOlF1YW5nMTIzNDU2"
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



