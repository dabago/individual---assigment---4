#%%

import requests

#
graph1= {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": [],
    "f": []
}

graph2 = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"]
}

graph = {} 
graph3 = []

graph4 = "afas"
graph5 = {"a": "b"}



def mycurrentgraph():
    request = requests.get("http://localhost:5000/mygraph").json()
    return request

def upload_graph(graph): 
    data = graph
    request = requests.post("http://localhost:5000/upload-graph", json=data).json()
    return request



def get_degrees_of_separation(origin, destination): 
    data = graph
    request = requests.get('http://localhost:5000/degrees-of-separation/{}/{}'.format(origin, destination), json=data).json()
    
    return request




