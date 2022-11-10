import requests
import os
from _datetime import datetime


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "achieverking01"
pixela_parameter = {
    "token": os.environ.get("PIXELA_TOKEN"),
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


"""creating a pixela graph"""
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
header = {
    "X-USER-TOKEN": os.environ.get("PIXELA_TOKEN"),
}
graph_parameter = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hour",
    "type": "int",
    "color": "sora",
}
"""Posting a Request"""
# graph = requests.post(url=GRAPH_ENDPOINT, json=graph_parameter, headers=header)
today = datetime.now()
today_date = today.strftime("20%y%m%d")

GRAPH_ENTRY = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"
entry_parameter = {
    "date": today_date,
    "quantity": "7",
}

# entry = requests.post(url=GRAPH_ENTRY, json=entry_parameter, headers=header)

"""Updating a post"""
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/20221109"
update_parameter = {
    "quantity": "7",
}

update = requests.put(url=UPDATE_ENDPOINT, json=update_parameter, headers=header)
print(update.text)
