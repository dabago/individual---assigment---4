#%%

import requests


def mygraph():
    data = graph
    request = requests.get("http://localhost:5000/mygraph", json=data)
    return request.json()
