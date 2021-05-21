import requests
from datetime import datetime

user_name = "tab"
token = "jennieee"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": token,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{user_name}/graphs"
graph_config = {
    "id": "graph1",
    "name": "ReadingBook",
    "unit": "commit",
    "type": "int",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# # TODO: Post a pixel
today = datetime.now()
print(today.strftime("%Y%m%d"))
post_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10"
}
# post_pixel = f"https://pixe.la/v1/users/{user_name}/graphs/{graph_config['id']}"
# response = requests.post(url=post_pixel, json=post_pixel_config, headers=headers)
# print(response.text)


