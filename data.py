import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}
data = requests.get(url=f"https://opentdb.com/api.php?", params=parameters)
data.raise_for_status()
data1 = data.json()

questions_data = data1["results"]

